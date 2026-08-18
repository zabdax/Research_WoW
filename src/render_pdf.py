import os
import markdown
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font
        self.set_font("Times", "I", 10)
        self.set_text_color(128, 128, 128)
        # Title
        self.cell(0, 10, "International Journal of Astrobiology - Draft", 0, 1, "R")

    def footer(self):
        self.set_y(-15)
        self.set_font("Times", "I", 10)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def generate_pdf():
    # Read the markdown
    md_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "manuscripts", "full_paper.md")
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # We need to inject the images into the markdown before converting to HTML.
    # The figures should go into "5. Results and Sensitivity Analysis" and "4. The 3-Pillar Validation Suite"
    
    # Inject Fig 2 into 4
    pillar_heading = "This comprehensive 3-pillar validation firmly establishes that our base likelihood emulator operates flawlessly."
    fig2_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures", "fig2_validation_pillars.png")
    # Replace backward slashes with forward slashes for HTML
    fig2_path = fig2_path.replace("\\", "/")
    
    fig2_md = f"\n<br>\n<center><img src='{fig2_path}' width='500'></center>\n<br><i>Figure 1: Visualization of the 3-Pillar Monte Carlo validation against K&G (2022) targets.</i>\n<br>"
    md_text = md_text.replace(pillar_heading, pillar_heading + "\n" + fig2_md)
    
    # Inject Fig 1 into 5
    sensitivity_heading = "H1 and H2 remained suppressed at ~0.00%, satisfying our baseline sanity checks for near-refuted models."
    fig1_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures", "fig1_sensitivity_sweep.png")
    fig1_path = fig1_path.replace("\\", "/")
    
    fig1_md = f"\n<br>\n<center><img src='{fig1_path}' width='500'></center>\n<br><i>Figure 2: Prior sensitivity sweep demonstrating the robust dominance of the H3 (HI Maser) model across a wide range of assumed prior probabilities.</i>\n<br>"
    md_text = md_text.replace(sensitivity_heading, sensitivity_heading + "\n" + fig1_md)

    # Convert to HTML
    html_content = markdown.markdown(md_text, extensions=['tables'])
    
    # Clean up math equations for FPDF (it doesn't natively render MathJax)
    # Convert $$...$$ and \xi to text representations
    html_content = html_content.replace(r"$$P(T \mid D, C) = \frac{P(T \mid C) \cdot \xi}{1 + P(T \mid C)(\xi - 1)}$$", 
                                        "<b>P(T | D, C) = [ P(T | C) * &xi; ] / [ 1 + P(T | C)(&xi; - 1) ]</b>")
    html_content = html_content.replace(r"\xi", "&xi;")
    html_content = html_content.replace(r"$$e^{-192h \times (0.121/24)} \approx 0.380$$",
                                        "<b>e^(-192 * 0.121/24) = 0.380</b>")
    html_content = html_content.replace(r"$30.5\sigma$", "30.5-sigma")
    html_content = html_content.replace(r"$\lambda = 0.121$", "&lambda; = 0.121")
    html_content = html_content.replace(r"$\sim 10$", "~10")

    # Wrap in a basic structure
    pdf = PDF()
    
    # Add Unicode font (Arial)
    font_path = r"C:\Windows\Fonts\arial.ttf"
    pdf.add_font("Arial", "", font_path)
    pdf.add_font("Arial", "I", r"C:\Windows\Fonts\ariali.ttf")
    pdf.add_font("Arial", "B", r"C:\Windows\Fonts\arialbd.ttf")
    
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Write HTML
    try:
        pdf.write_html(html_content)
    except Exception as e:
        print(f"Error during HTML writing: {e}")
        
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "manuscripts", "Wow_Signal_IJA_Manuscript.pdf")
    pdf.output(out_path)
    print(f"Generated PDF at: {out_path}")

if __name__ == "__main__":
    generate_pdf()
