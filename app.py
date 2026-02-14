import gradio as gr
import os

# =========================
# Language Extensions
# =========================
EXTENSIONS = {
    "Python": ".py",
    "C": ".c",
    "C++": ".cpp",
    "Java": ".java",
    "JavaScript": ".js"
}

# =========================
# CSS for custom dark theme
# =========================
custom_css = """
body { background: #0f172a !important; font-family: 'Inter', sans-serif; }
.gradio-container { max-width: 100% !important; padding: 16px !important; background: #0f172a !important; }
h1 { font-size: 28px !important; font-weight: 700 !important; color: #f8fafc !important; text-align: center !important; }
p, label { color: #cbd5e1 !important; }
.block { background: #1e293b !important; border-radius: 16px !important; padding: 24px !important; margin: 8px !important; }
button { background: linear-gradient(135deg,#2563eb,#1d4ed8)!important; color:white!important; border-radius:14px!important; border:none!important; }
footer { display:none !important; }
"""

# =========================
# Functions
# =========================
def refine_code(code, language):
    refined = f"# Refined {language} code\n{code.upper()}"
    filename = f"refined_code{EXTENSIONS.get(language,'.txt')}"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(refined)
    return filename

def optimize_code(code, language):
    optimized = f"# Optimized {language} code\n{code[::-1]}"
    filename = f"optimized_code{EXTENSIONS.get(language,'.txt')}"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(optimized)
    return filename

def convert_code(code, from_lang, to_lang):
    converted = f"# Converted from {from_lang} to {to_lang}\n{code}"
    filename = f"converted_code{EXTENSIONS.get(to_lang,'.txt')}"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(converted)
    return filename

# =========================
# UI Layout
# =========================
with gr.Blocks(css=custom_css) as app:

    # FRONT PAGE
    with gr.Column(visible=True) as front_page:
        gr.Markdown("# 🚀 CodeRefine AI")
        gr.Markdown("AI-powered code analysis & conversion")

        with gr.Row():
            refine_btn = gr.Button("✨ Refine Code", elem_classes="block")
            optimize_btn = gr.Button("⚡ Optimize Code", elem_classes="block")
            convert_btn = gr.Button("🔄 Convert Code", elem_classes="block")

    # REFINE PAGE
    with gr.Column(visible=False) as refine_page:
        gr.Markdown("# ✨ Refine Code")
        code_r = gr.Textbox(label="Enter code", lines=10)
        lang_r = gr.Dropdown(list(EXTENSIONS.keys()), label="Language")
        file_r = gr.File(label="Download Refined Code")
        gr.Button("Refine").click(refine_code, [code_r, lang_r], file_r)
        back_r = gr.Button("⬅ Back")

    # OPTIMIZE PAGE
    with gr.Column(visible=False) as optimize_page:
        gr.Markdown("# ⚡ Optimize Code")
        code_o = gr.Textbox(label="Enter code", lines=10)
        lang_o = gr.Dropdown(list(EXTENSIONS.keys()), label="Language")
        file_o = gr.File(label="Download Optimized Code")
        gr.Button("Optimize").click(optimize_code, [code_o, lang_o], file_o)
        back_o = gr.Button("⬅ Back")

    # CONVERT PAGE
    with gr.Column(visible=False) as convert_page:
        gr.Markdown("# 🔄 Convert Code")
        code_c = gr.Textbox(label="Enter code", lines=10)
        from_l = gr.Dropdown(list(EXTENSIONS.keys()), label="From")
        to_l = gr.Dropdown(list(EXTENSIONS.keys()), label="To")
        file_c = gr.File(label="Download Converted Code")
        gr.Button("Convert").click(convert_code, [code_c, from_l, to_l], file_c)
        back_c = gr.Button("⬅ Back")

    # =========================
    # Navigation functions
    # =========================
    def show_refine(): return False, True, False, False
    def show_optimize(): return False, False, True, False
    def show_convert(): return False, False, False, True
    def show_home(): return True, False, False, False

    refine_btn.click(show_refine, outputs=[front_page, refine_page, optimize_page, convert_page])
    optimize_btn.click(show_optimize, outputs=[front_page, refine_page, optimize_page, convert_page])
    convert_btn.click(show_convert, outputs=[front_page, refine_page, optimize_page, convert_page])

    back_r.click(show_home, outputs=[front_page, refine_page, optimize_page, convert_page])
    back_o.click(show_home, outputs=[front_page, refine_page, optimize_page, convert_page])
    back_c.click(show_home, outputs=[front_page, refine_page, optimize_page, convert_page])

# =========================
# Render Deployment Launch
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.launch(server_name="0.0.0.0", server_port=port)
