from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "KC_高齊_履歷與作品集摘要.pdf"
FONT = r"C:\Windows\Fonts\msjh.ttc"
FONT_BOLD = r"C:\Windows\Fonts\msjhbd.ttc"

pdfmetrics.registerFont(TTFont("MSJH", FONT, subfontIndex=0))
pdfmetrics.registerFont(TTFont("MSJH-Bold", FONT_BOLD, subfontIndex=0))

INK = HexColor("#141311")
PAPER = HexColor("#F6F3EE")
GOLD = HexColor("#B58D49")
MUTED = HexColor("#625D54")
LINE = HexColor("#D9D1C5")


def wrap(text, font, size, width):
    lines, line = [], ""
    for char in text:
        candidate = line + char
        if line and pdfmetrics.stringWidth(candidate, font, size) > width:
            lines.append(line)
            line = char
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def text_block(c, text, x, y, width, font="MSJH", size=9.2, leading=14, color=INK):
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def section_label(c, label, x, y, width):
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.1)
    c.line(x, y + 5, x + 23, y + 5)
    c.setFillColor(GOLD)
    c.setFont("MSJH-Bold", 8.4)
    c.drawString(x + 31, y, label)
    c.setStrokeColor(LINE)
    c.setLineWidth(.45)
    c.line(x, y - 8, x + width, y - 8)
    return y - 24


def bullet(c, title, copy, x, y, width):
    c.setFillColor(GOLD)
    c.circle(x + 3, y + 1, 1.5, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 9.1)
    c.drawString(x + 12, y - 2, title)
    return text_block(c, copy, x + 12, y - 17, width - 12, size=8.5, leading=12.5, color=MUTED) - 7


def experience(c, company, role, copy, x, y, width):
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 9.2)
    c.drawString(x, y, company)
    c.setFillColor(GOLD)
    c.setFont("MSJH", 8.5)
    c.drawRightString(x + width, y, role)
    y = text_block(c, copy, x, y - 14, width, size=8.35, leading=11.5, color=MUTED)
    c.setStrokeColor(LINE)
    c.setLineWidth(.35)
    c.line(x, y - 4, x + width, y - 4)
    return y - 13


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4)
    w, h = A4
    c.setTitle("KC 高齊｜履歷與作品集摘要")
    c.setAuthor("高齊 KC")

    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(INK)
    c.rect(0, h - 138, w, 138, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(42, h - 104, 64, 2, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("MSJH-Bold", 28)
    c.drawString(42, h - 75, "高齊  KC")
    c.setFillColor(GOLD)
    c.setFont("MSJH", 11)
    c.drawString(42, h - 98, "品牌視覺  ·  內容企劃  ·  行銷支援")
    c.setFillColor(HexColor("#EAE4D9"))
    c.setFont("MSJH", 8.7)
    c.drawRightString(w - 42, h - 62, "chi093093chi@gmail.com")
    c.drawRightString(w - 42, h - 80, "0905 581 266")
    c.drawRightString(w - 42, h - 98, "kc09393.github.io/kc-portfolio")

    left_x, left_w = 42, 162
    right_x, right_w = 232, 321
    y_left = h - 166
    y_right = h - 166

    y_left = section_label(c, "求職方向", left_x, y_left, left_w)
    y_left = bullet(c, "品牌與商品視覺", "主視覺、商品素材、活動宣傳與延伸應用。", left_x, y_left, left_w)
    y_left = bullet(c, "社群與活動內容", "整理溝通重點、內容順序與發布前素材。", left_x, y_left, left_w)
    y_left = bullet(c, "3D 視覺製作", "以 Blender 製作角色、產品與情境畫面。", left_x, y_left, left_w)

    y_left -= 9
    y_left = section_label(c, "工具", left_x, y_left, left_w)
    c.setFillColor(MUTED)
    c.setFont("MSJH", 8.65)
    for tool_line in ["Photoshop · Illustrator", "Lightroom · InDesign", "Canva · Figma · Blender", "Procreate"]:
        c.drawString(left_x, y_left, tool_line)
        y_left -= 13
    y_left -= 10

    y_left = section_label(c, "學歷", left_x, y_left, left_w)
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 9)
    c.drawString(left_x, y_left, "嶺東科技大學｜時尚經營系")
    c.setFillColor(MUTED)
    c.setFont("MSJH", 8.4)
    c.drawString(left_x, y_left - 14, "大學畢業")
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 9)
    c.drawString(left_x, y_left - 42, "中華藝術學校｜美術科")
    c.setFillColor(MUTED)
    c.setFont("MSJH", 8.4)
    c.drawString(left_x, y_left - 56, "高中畢業")

    y_left -= 88
    y_left = section_label(c, "證照與能力佐證", left_x, y_left, left_w)
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 7.8)
    c.drawString(left_x, y_left, "Adobe Certified Professional")
    c.setFillColor(MUTED)
    c.setFont("MSJH", 7.55)
    c.drawString(left_x, y_left - 11, "Illustrator、Photoshop、Visual Designer")
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 7.8)
    c.drawString(left_x, y_left - 27, "勞動部丙級技術士")
    c.setFillColor(MUTED)
    c.setFont("MSJH", 7.55)
    c.drawString(left_x, y_left - 38, "視覺傳達設計／電腦軟體應用")
    c.setFillColor(INK)
    c.setFont("MSJH-Bold", 7.8)
    c.drawString(left_x, y_left - 54, "TQC+ 影像編輯製作｜色彩規劃管理師")
    c.setFillColor(MUTED)
    c.setFont("MSJH", 7.55)
    c.drawString(left_x, y_left - 70, "水上安全救生員證｜基本救命術（BLS）")
    c.drawString(left_x, y_left - 81, "服務業管理師｜時尚產業實習課程結業")

    y_right = section_label(c, "個人摘要", right_x, y_right, right_w)
    y_right = text_block(c, "畢業於嶺東科技大學時尚經營系。擅長先釐清品牌要說什麼、給誰看，再把零散需求整理為清楚的視覺、文字與可執行內容流程；具備零售現場、社群素材與活動支援經驗。", right_x, y_right, right_w, size=9.3, leading=14.5, color=INK) - 12

    y_right = section_label(c, "相關經歷", right_x, y_right, right_w)
    y_right = experience(c, "首爾蝶衣韓系服裝", "後台管理／美術編輯", "商品資料整理與上架、視覺素材製作、社群內容編排。", right_x, y_right, right_w)
    y_right = experience(c, "鹿角寵物零食", "行銷規劃／美術編輯", "參與社群內容、廣告素材與促銷視覺製作。", right_x, y_right, right_w)
    y_right = experience(c, "安心家農業", "企劃／設計人員", "協助活動企劃、行銷物料、流程整理與現場支援。", right_x, y_right, right_w)
    y_right = experience(c, "新光三越・DYCTEAM", "專櫃銷售", "顧客接待、商品介紹、陳列與日常營運支援。", right_x, y_right, right_w)
    y_right = experience(c, "新光三越・Porter & Hunter", "專櫃工讀", "顧客接待、商品介紹與零售現場作業。", right_x, y_right, right_w)

    y_right -= 3
    y_right = section_label(c, "精選作品", right_x, y_right, right_w)
    y_right = bullet(c, "元福宙畢業展｜主視覺與專刊", "美宣分工，參與主視覺、海報與 25 頁專刊視覺整理。", right_x, y_right, right_w)
    y_right = bullet(c, "Y／Z 世代香水偏好研究", "團隊研究，207 份有效問卷的消費者洞察整理。", right_x, y_right, right_w)
    y_right = bullet(c, "Blender 材質節點學習站", "個人雙語互動學習網站：內容架構、介面與操作流程規劃。", right_x, y_right, right_w)

    c.setStrokeColor(GOLD)
    c.setLineWidth(.7)
    c.line(42, 35, w - 42, 35)
    c.setFillColor(MUTED)
    c.setFont("MSJH", 7.5)
    c.drawString(42, 21, "完整作品集：kc09393.github.io/kc-portfolio/")
    c.drawRightString(w - 42, 21, "KC 高齊｜履歷與作品集摘要")
    c.save()


if __name__ == "__main__":
    main()
