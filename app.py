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
/* Background */
body {
    background: #0f172a !important;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
.gradio-container {
    max-width: 100% !important;
    padding: 16px !important;
    background: #0f172a !important;
}
h1 {
    font-size: 28px !important;
    font-weight: 700 !important;
    color: #f8fafc !important;
    text-align: center !important;
    margin-bottom: 16px !important;
}
p, label {
    color: #cbd5e1 !important;
    font-size: 14px !important;
}
.block {
    background: #1e293b !important;
    border-radius: 16px !important;
    padding: 24px !important;
    margin: 8px !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35) !important;
    text-align: center !important;
    cursor: pointer;
    transition: all 0.2s ease-in-out !important;
}
.block:hover {
    transform: scale(1.03);
}
textarea, input, select {
    background: #111827 !important;
    color: #f1f5f9 !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 15px !important;
}
button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border-radius: 14px !important;
    border: none !important;
    padding: 14px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 100% !important;
    min-height: 48px !important;
    transition: all 0.2s ease-in-out !important;
}
button:hover {
    transform: scale(1.02);
}
footer {
    display: none !important;
}
"""

# =========================
# Functions for app
# =========================
def refine_code(code, language):
    refined = f"# Refined {language} code\n{code.upper()}"
    filename = f"refined_code{EXTENSIONS.get(language, '.txt')}"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(refined)
    return filename

def optimize_code(code, language):
    optimized = f"# Optimized {language} code\n{code[::-1]}"
    filename = f"optimized_code{EXTENSIONS.get(language, '.txt')}"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(optimized)
    return filename

def convert_code(code, from_lang, to_lang):
    converted = f"# Converted from {from_lang} to {to_lang}\n{code}"
    filename = f"converted_code{EXTENSIONS.get(to_lang, '.txt')}"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(converted)
    return filename

# =========================
# App layout
# =========================
with gr.Blocks(css=custom_css) as app:

    # --- Front page ---
    with gr.Column(visible=True) as front_page:
        gr.Markdown("# 🚀 CodeRefine AI")
        gr.Markdown("AI-powered code analysis & conversion")
        with gr.Row():
            refine_block = gr.Box("✨ Refine Code", elem_classes="block")
            optimize_block = gr.Box("⚡ Optimize Code", elem_classes="block")
            convert_block = gr.Box("🔄 Convert Code", elem_classes="block")

    # --- Refine page ---
    with gr.Column(visible=False) as refine_page:
        gr.Markdown("# ✨ Refine Code")
        code_input_refine = gr.Textbox(label="Enter code", lines=10)
        lang_input_refine = gr.Dropdown(list(EXTENSIONS.keys()), label="Language")
        refine_output = gr.File(label="Download Refined Code")
        gr.Button("Refine Code").click(
            refine_code,
            inputs=[code_input_refine, lang_input_refine],
            outputs=refine_output
        )
        back_refine = gr.Button("⬅ Back to Home")
    
    # --- Optimize page ---
    with gr.Column(visible=False) as optimize_page:
        gr.Markdown("# ⚡ Optimize Code")
        code_input_optimize = gr.Textbox(label="Enter code", lines=10)
        lang_input_optimize = gr.Dropdown(list(EXTENSIONS.keys()), label="Language")
        optimize_output = gr.File(label="Download Optimized Code")
        gr.Button("Optimize Code").click(
            optimize_code,
            inputs=[code_input_optimize, lang_input_optimize],
            outputs=optimize_output
        )
        back_optimize = gr.Button("⬅ Back to Home")

    # --- Convert page ---
    with gr.Column(visible=False) as convert_page:
        gr.Markdown("# 🔄 Convert Code")
        code_input_convert = gr.Textbox(label="Enter code", lines=10)
        from_lang_input = gr.Dropdown(list(EXTENSIONS.keys()), label="From Language")
        to_lang_input = gr.Dropdown(list(EXTENSIONS.keys()), label="To Language")
        convert_output = gr.File(label="Download Converted Code")
        gr.Button("Convert Code").click(
            convert_code,
            inputs=[code_input_convert, from_lang_input, to_lang_input],
            outputs=convert_output
        )
        back_convert = gr.Button("⬅ Back to Home")

    # =========================
    # Navigation functions
    # =========================
    def show_refine():
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

    def show_optimize():
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

    def show_convert():
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)

    def show_front():
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

    # Connect navigation
    refine_block.click(show_refine, outputs=[front_page, refine_page, optimize_page, convert_page])
    optimize_block.click(show_optimize, outputs=[front_page, refine_page, optimize_page, convert_page])
    convert_block.click(show_convert, outputs=[front_page, refine_page, optimize_page, convert_page])

    back_refine.click(show_front, outputs=[front_page, refine_page, optimize_page, convert_page])
    back_optimize.click(show_front, outputs=[front_page, refine_page, optimize_page, convert_page])
    back_convert.click(show_front, outputs=[front_page, refine_page, optimize_page, convert_page])

# Launch app
app.launch()
