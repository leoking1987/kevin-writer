#!/usr/bin/env python3
"""
Reusable landscape side-by-side comparison .docx generator for kevin-script-v2.

Usage:
    python3 render_comparison_docx.py <input.json> <output.docx>

Input JSON schema:
{
  "title": "2027湾区房价预测：大盘平稳，冷热悬殊",
  "subtitle": "原稿 vs 改写版 左右对照稿   |   原稿：@xxx   |   改写原则：真诚立场 · 客观分析 · 保留全部硬数据",
  "header_text": "Kevin Mo 湾区房产脚本改写对照   ·   核心定调：大盘平稳，冷热悬殊",
  "footer_prefix": "2027湾区房价预测 · 左右对照改写稿",
  "highlight_phrase": "大盘平稳，冷热悬殊",
  "summary_cards": [
    ["核心定调更新", "..."],
    ["字数与时长压缩", "AUTO"],
    ["核心结构升级", "..."],
    ["待补数据提醒", "..."]
  ],
  "sections": [
    {
      "banner": "第一幕：...",
      "rows": [
        {
          "label": "1.1 小节名",
          "left": ["原稿段落1", "原稿段落2"],
          "right": ["改写段落1", "改写段落2"]
        }
      ]
    }
  ]
}
"""

import json
import os
import re
import sys
import zipfile
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

FONT_NAME = "PingFang SC"

NAVY = "1B365D"
SLATE_SUB = "2E4E7E"
LEFT_BG = "F6F7F9"
RIGHT_BG = "FFFFFF"
SUMMARY_BG = "F0F4FA"
BORDER_COLOR = "D5DCE6"
TEXT_DARK = RGBColor(0x1E, 0x29, 0x3B)
TEXT_MUTED = RGBColor(0x47, 0x55, 0x69)
TEXT_LIGHT = RGBColor(0x64, 0x74, 0x8B)
ACCENT_NAVY = RGBColor(0x1B, 0x36, 0x5D)
ACCENT_AMBER = RGBColor(0xB4, 0x53, 0x09)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def count_spoken_chars(paras):
    text = "".join(paras)
    cleaned = re.sub(r"（(?:注|原稿批注)：[^）]*）", "", text)
    cleaned = re.sub(r"【[^】]*】", "", cleaned)
    cleaned = re.sub(r"\[[^\]]*\]", "", cleaned)
    cjk = re.findall(r"[\u4e00-\u9fff]", cleaned)
    alnum = re.findall(r"[A-Za-z0-9]+(?:[.,%-][A-Za-z0-9]+)*", cleaned)
    return len(cjk) + len(alnum)


def set_cell_shading(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:color="auto" w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=110, bottom=110, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for side, val in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        node = OxmlElement(f"w:{side}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side, spec in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        if spec is None:
            continue
        b = OxmlElement(f"w:{side}")
        val, sz, color = spec
        b.set(qn("w:val"), val)
        if sz:
            b.set(qn("w:sz"), str(sz))
        if color:
            b.set(qn("w:color"), color)
        b.set(qn("w:space"), "0")
        tcBorders.append(b)
    tcPr.append(tcBorders)


def set_cell_width(cell, dxa):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = OxmlElement("w:tcW")
    tcW.set(qn("w:w"), str(dxa))
    tcW.set(qn("w:type"), "dxa")
    tcPr.append(tcW)


def set_row_header(row):
    row._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))


def set_row_cant_split(row):
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def add_run_styled(p, text, size=9.5, bold=False, color=TEXT_DARK):
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.name = FONT_NAME
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), FONT_NAME)
    return run


def add_rich_paragraph(cell, text, highlight_phrase="", size=9.5, color=TEXT_DARK, space_after=4, first_in_cell=False):
    p = cell.paragraphs[0] if first_in_cell else cell.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.35

    patterns = [r"【[^】]+】", r"\[[^\]]+\]"]
    if highlight_phrase:
        patterns.append(re.escape(highlight_phrase))
    token_re = re.compile("(" + "|".join(patterns) + ")")

    for part in token_re.split(text):
        if not part:
            continue
        if part.startswith("【待补"):
            add_run_styled(p, part, size=size, bold=True, color=ACCENT_AMBER)
        elif part.startswith("【") and part.endswith("】"):
            add_run_styled(p, part, size=size, bold=True, color=ACCENT_NAVY)
        elif part.startswith("[") and part.endswith("]"):
            add_run_styled(p, part, size=size - 0.5, bold=False, color=TEXT_LIGHT)
        elif highlight_phrase and part == highlight_phrase:
            add_run_styled(p, part, size=size, bold=True, color=ACCENT_NAVY)
        else:
            add_run_styled(p, part, size=size, bold=False, color=color)
    return p


def strip_zip_dir_entries(docx_path):
    tmp_path = docx_path + ".tmp"
    with zipfile.ZipFile(docx_path, "r") as zin, zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename.endswith("/"):
                continue
            zout.writestr(item, zin.read(item.filename))
    os.replace(tmp_path, docx_path)


def build_docx(spec, output_path):
    orig_all, rewr_all = [], []
    for sec in spec["sections"]:
        for row in sec["rows"]:
            orig_all.extend(row["left"])
            rewr_all.extend(row["right"])

    orig_chars = count_spoken_chars(orig_all)
    rewr_chars = count_spoken_chars(rewr_all)
    delta_pct = (1 - rewr_chars / orig_chars) * 100 if orig_chars else 0.0
    delta_label = f"精简 {delta_pct:.0f}%" if delta_pct >= 0 else f"增加 {-delta_pct:.0f}%"
    auto_summary = f"约 {orig_chars:,} 字（{orig_chars/315:.1f}分）→ 约 {rewr_chars:,} 字（{rewr_chars/315:.1f}分），{delta_label}"

    doc = Document()
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(11.0)
    section.page_height = Inches(8.5)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)

    # Header & Footer
    hp = section.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_run_styled(hp, spec.get("header_text", spec["title"]), size=8.5, color=TEXT_LIGHT)

    fp = section.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    add_run_styled(fp, f"{spec.get('footer_prefix', spec['title'])}   |   第 ", size=8.5, color=TEXT_LIGHT)
    fld1 = OxmlElement("w:fldSimple")
    fld1.set(qn("w:instr"), "PAGE")
    fp._p.append(fld1)
    add_run_styled(fp, " 页 / 共 ", size=8.5, color=TEXT_LIGHT)
    fld2 = OxmlElement("w:fldSimple")
    fld2.set(qn("w:instr"), "NUMPAGES")
    fp._p.append(fld2)
    add_run_styled(fp, " 页", size=8.5, color=TEXT_LIGHT)

    # Default style
    normal = doc.styles["Normal"]
    normal.font.name = FONT_NAME
    normal.font.size = Pt(9.5)
    normal.font.color.rgb = TEXT_DARK
    rPr = normal.element.get_or_add_rPr()
    rFonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), FONT_NAME)
    rPr.insert(0, rFonts)

    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    add_run_styled(p_title, spec["title"], size=18, bold=True, color=ACCENT_NAVY)

    if spec.get("subtitle"):
        p_sub = doc.add_paragraph()
        p_sub.paragraph_format.space_before = Pt(0)
        p_sub.paragraph_format.space_after = Pt(8)
        add_run_styled(p_sub, spec["subtitle"], size=9, color=TEXT_MUTED)

    TOTAL_DXA = 14256
    cards = spec.get("summary_cards") or []
    if cards:
        n_cols = len(cards)
        col_w = TOTAL_DXA // n_cols
        sum_tbl = doc.add_table(rows=1, cols=n_cols)
        sum_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        sum_tbl.autofit = False
        s_pr = sum_tbl._tbl.tblPr
        s_layout = OxmlElement("w:tblLayout")
        s_layout.set(qn("w:type"), "fixed")
        s_pr.append(s_layout)
        s_w = OxmlElement("w:tblW")
        s_w.set(qn("w:w"), str(TOTAL_DXA))
        s_w.set(qn("w:type"), "dxa")
        s_pr.append(s_w)

        for idx, (label, val) in enumerate(cards):
            cell = sum_tbl.rows[0].cells[idx]
            w = col_w if idx < n_cols - 1 else TOTAL_DXA - col_w * (n_cols - 1)
            set_cell_width(cell, w)
            set_cell_shading(cell, SUMMARY_BG)
            set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
            set_cell_borders(
                cell,
                top=("single", 6, NAVY),
                bottom=("single", 4, BORDER_COLOR),
                left=("single", 4, BORDER_COLOR),
                right=("single", 4, BORDER_COLOR),
            )
            p1 = cell.paragraphs[0]
            p1.paragraph_format.space_before = Pt(0)
            p1.paragraph_format.space_after = Pt(2)
            add_run_styled(p1, label, size=8.5, bold=True, color=ACCENT_NAVY)
            p2 = cell.add_paragraph()
            p2.paragraph_format.space_before = Pt(0)
            p2.paragraph_format.space_after = Pt(0)
            p2.paragraph_format.line_spacing = 1.25
            text_val = auto_summary if val == "AUTO" else val
            is_todo = "待补" in label
            add_run_styled(p2, text_val, size=8.5, color=ACCENT_AMBER if is_todo else TEXT_DARK)

        sp = doc.add_paragraph()
        sp.paragraph_format.space_before = Pt(0)
        sp.paragraph_format.space_after = Pt(6)

    # Main 3-column comparison table
    COL_WIDTHS = [1440, 6408, 6408]
    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    m_pr = table._tbl.tblPr
    m_layout = OxmlElement("w:tblLayout")
    m_layout.set(qn("w:type"), "fixed")
    m_pr.append(m_layout)
    m_w = OxmlElement("w:tblW")
    m_w.set(qn("w:w"), str(TOTAL_DXA))
    m_w.set(qn("w:type"), "dxa")
    m_pr.append(m_w)
    for gridCol, w in zip(table._tbl.tblGrid.findall(qn("w:gridCol")), COL_WIDTHS):
        gridCol.set(qn("w:w"), str(w))

    hdr_row = table.rows[0]
    set_row_header(hdr_row)
    set_row_cant_split(hdr_row)
    for idx, title_text in enumerate(["板块 / 节点", "原稿", "改写版（真诚 · 客观 · 高信息密度）"]):
        cell = hdr_row.cells[idx]
        set_cell_width(cell, COL_WIDTHS[idx])
        set_cell_shading(cell, NAVY)
        set_cell_margins(cell, top=110, bottom=110, left=130, right=130)
        set_cell_borders(
            cell,
            top=("single", 6, NAVY),
            bottom=("single", 8, NAVY),
            left=("single", 4, NAVY),
            right=("single", 4, NAVY),
        )
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        add_run_styled(p, title_text, size=10, bold=True, color=WHITE)

    highlight_phrase = spec.get("highlight_phrase", "")
    for sec in spec["sections"]:
        banner_row = table.add_row()
        set_row_cant_split(banner_row)
        merged = banner_row.cells[0].merge(banner_row.cells[2])
        set_cell_width(merged, TOTAL_DXA)
        set_cell_shading(merged, SLATE_SUB)
        set_cell_margins(merged, top=90, bottom=90, left=140, right=140)
        set_cell_borders(
            merged,
            top=("single", 6, NAVY),
            bottom=("single", 6, NAVY),
            left=("single", 4, SLATE_SUB),
            right=("single", 4, SLATE_SUB),
        )
        bp = merged.paragraphs[0]
        bp.paragraph_format.space_before = Pt(0)
        bp.paragraph_format.space_after = Pt(0)
        bp.paragraph_format.keep_with_next = True
        add_run_styled(bp, sec["banner"], size=10.5, bold=True, color=WHITE)

        for row_item in sec["rows"]:
            row = table.add_row()
            set_row_cant_split(row)

            c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
            set_cell_width(c0, COL_WIDTHS[0])
            set_cell_shading(c0, LEFT_BG)
            set_cell_margins(c0, top=110, bottom=110, left=110, right=110)
            set_cell_borders(c0, top=("single", 4, BORDER_COLOR), bottom=("single", 4, BORDER_COLOR), left=("single", 4, BORDER_COLOR), right=("single", 4, BORDER_COLOR))
            c0.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_before = Pt(0)
            p0.paragraph_format.space_after = Pt(4)
            p0.paragraph_format.line_spacing = 1.25
            add_run_styled(p0, row_item["label"], size=8.8, bold=True, color=ACCENT_NAVY)

            l_cnt = count_spoken_chars(row_item["left"])
            r_cnt = count_spoken_chars(row_item["right"])
            for txt, after in ((f"原 {l_cnt} 字", 1), (f"改 {r_cnt} 字", 0)):
                pm = c0.add_paragraph()
                pm.paragraph_format.space_before = Pt(0)
                pm.paragraph_format.space_after = Pt(after)
                pm.paragraph_format.line_spacing = 1.15
                add_run_styled(pm, txt, size=7.8, color=TEXT_LIGHT)

            set_cell_width(c1, COL_WIDTHS[1])
            set_cell_shading(c1, LEFT_BG)
            set_cell_margins(c1, top=110, bottom=110, left=140, right=140)
            set_cell_borders(c1, top=("single", 4, BORDER_COLOR), bottom=("single", 4, BORDER_COLOR), left=("single", 4, BORDER_COLOR), right=("single", 8, BORDER_COLOR))
            c1.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            for i, text in enumerate(row_item["left"]):
                add_rich_paragraph(c1, text, highlight_phrase=highlight_phrase, size=9.2, color=TEXT_MUTED, space_after=5 if i < len(row_item["left"]) - 1 else 0, first_in_cell=(i == 0))

            set_cell_width(c2, COL_WIDTHS[2])
            set_cell_shading(c2, RIGHT_BG)
            set_cell_margins(c2, top=110, bottom=110, left=140, right=140)
            set_cell_borders(c2, top=("single", 4, BORDER_COLOR), bottom=("single", 4, BORDER_COLOR), left=("single", 8, NAVY), right=("single", 4, BORDER_COLOR))
            c2.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            for i, text in enumerate(row_item["right"]):
                add_rich_paragraph(c2, text, highlight_phrase=highlight_phrase, size=9.5, color=TEXT_DARK, space_after=5 if i < len(row_item["right"]) - 1 else 0, first_in_cell=(i == 0))

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc.save(output_path)
    strip_zip_dir_entries(output_path)
    print(f"Saved: {output_path}")
    print(f"Original: {orig_chars} chars (~{orig_chars/315:.1f} min) | Rewritten: {rewr_chars} chars (~{rewr_chars/315:.1f} min, {delta_label})")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 render_comparison_docx.py <input.json> <output.docx>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        spec = json.load(f)
    build_docx(spec, sys.argv[2])


if __name__ == "__main__":
    main()
