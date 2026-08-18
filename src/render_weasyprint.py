import os
import markdown
from weasyprint import HTML, CSS

def generate_pdf():
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_path = os.path.join(base_dir, "manuscripts", "full_paper.md")
    fig1_path = os.path.join(base_dir, "figures", "fig1_sensitivity_sweep.png")
    fig2_path = os.path.join(base_dir, "figures", "fig2_validation_pillars.png")
    out_path = os.path.join(base_dir, "manuscripts", "Wow_Signal_IJA_Manuscript.pdf")

    # Read markdown
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Inject Images
    # Fig 2 into Section 4
    pillar_heading = "This comprehensive 3-pillar validation firmly establishes that our base likelihood emulator operates flawlessly."
    # Path must be absolute file URI for WeasyPrint
    fig2_uri = f"file:///{fig2_path.replace(chr(92), '/')}"
    fig2_md = f"\n<figure style='text-align: center;'>\n  <img src='{fig2_uri}' style='width: 80%; max-width: 600px; border: 1px solid #ccc;' />\n  <figcaption style='font-style: italic; font-size: 0.9em; margin-top: 10px;'>Figure 1: Visualization of the 3-Pillar Monte Carlo validation against K&G (2022) targets.</figcaption>\n</figure>\n"
    md_text = md_text.replace(pillar_heading, pillar_heading + "\n" + fig2_md)
    
    # Fig 1 into Section 5
    sensitivity_heading = "H1 and H2 remained suppressed at ~0.00%, satisfying our baseline sanity checks for near-refuted models."
    fig1_uri = f"file:///{fig1_path.replace(chr(92), '/')}"
    fig1_md = f"\n<figure style='text-align: center;'>\n  <img src='{fig1_uri}' style='width: 80%; max-width: 600px; border: 1px solid #ccc;' />\n  <figcaption style='font-style: italic; font-size: 0.9em; margin-top: 10px;'>Figure 2: Prior sensitivity sweep demonstrating the robust dominance of the H3 (HI Maser) model across a wide range of assumed prior probabilities.</figcaption>\n</figure>\n"
    md_text = md_text.replace(sensitivity_heading, sensitivity_heading + "\n" + fig1_md)

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['tables'])

    # Format math blocks nicely for standard HTML (weasyprint doesn't natively parse MathJax, so we stylize it)
    html_content = html_content.replace(r"$$P(T \mid D, C) = \frac{P(T \mid C) \cdot \xi}{1 + P(T \mid C)(\xi - 1)}$$", 
                                        "<div class='math'>P(T | D, C) = [ P(T | C) &middot; &xi; ] / [ 1 + P(T | C)(&xi; - 1) ]</div>")
    html_content = html_content.replace(r"$$e^{-192h \times (0.121/24)} \approx 0.380$$",
                                        "<div class='math'>e<sup>-192h &times; (0.121/24)</sup> &approx; 0.380</div>")
    
    # Fix inline math
    html_content = html_content.replace(r"\xi", "&xi;")
    html_content = html_content.replace(r"$30.5\sigma$", "30.5&sigma;")
    html_content = html_content.replace(r"$\lambda = 0.121$", "&lambda; = 0.121")
    html_content = html_content.replace(r"$\sim 10$", "~10")

    # Define beautiful academic CSS
    css_string = """
    @page {
        size: A4;
        margin: 2.5cm;
        @bottom-center {
            content: counter(page);
            font-family: "Times New Roman", serif;
            font-size: 10pt;
        }
        @top-right {
            content: "International Journal of Astrobiology - Draft";
            font-family: "Times New Roman", serif;
            font-size: 9pt;
            color: #555;
        }
    }
    body {
        font-family: "Times New Roman", Times, serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #000;
        text-align: justify;
    }
    h1 {
        font-size: 18pt;
        text-align: center;
        margin-bottom: 0.5cm;
    }
    h2 {
        font-size: 14pt;
        margin-top: 1cm;
        border-bottom: 1px solid #000;
        padding-bottom: 2px;
    }
    h3 {
        font-size: 12pt;
        font-style: italic;
    }
    p {
        margin-bottom: 0.4cm;
    }
    .math {
        text-align: center;
        font-family: "Courier New", monospace;
        font-size: 11pt;
        margin: 10px 0;
        padding: 10px;
        background-color: #f9f9f9;
        border: 1px solid #eee;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    th, td {
        border-bottom: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        border-top: 2px solid #000;
        border-bottom: 2px solid #000;
        font-weight: bold;
    }
    ul, ol {
        margin-bottom: 0.4cm;
    }
    li {
        margin-bottom: 0.2cm;
    }
    """

    # Wrap in HTML body
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Wow! Signal Manuscript</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Render PDF
    HTML(string=full_html, base_url=base_dir).write_pdf(
        out_path,
        stylesheets=[CSS(string=css_string)]
    )
    print(f"Generated gorgeous PDF at: {out_path}")

if __name__ == "__main__":
    generate_pdf()
