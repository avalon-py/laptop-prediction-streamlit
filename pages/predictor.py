import streamlit as st
import pandas as pd
import joblib
import math
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# ── Model loader (cached) ─────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    import __main__
    from functions import to_str, ResolutionToPixels, VramEncoder, MultiHotEncoder
    __main__.to_str = to_str
    __main__.ResolutionToPixels = ResolutionToPixels
    __main__.VramEncoder = VramEncoder
    __main__.MultiHotEncoder = MultiHotEncoder

    model_path = os.path.join(os.path.dirname(__file__), "..", "model.pkl")
    if not os.path.exists(model_path):
        return None
    pipeline = joblib.load(model_path)

    # Disable multiprocessing for single-row inference
    for _, step in pipeline.steps:
        if hasattr(step, 'n_jobs'):
            step.n_jobs = 1
        if hasattr(step, 'regressor'):
            reg = step.regressor
            if hasattr(reg, 'n_jobs'):
                reg.n_jobs = 1
            if hasattr(reg, 'estimators_'):
                for est in reg.estimators_:
                    if hasattr(est, 'n_jobs'):
                        est.n_jobs = 1

    return pipeline

# ── Gauge SVG ─────────────────────────────────────────────────────────────────
def make_gauge(price: float, min_price: float = 1_000_000, max_price: float = 60_000_000) -> str:
    r = 90
    circumference = 2 * math.pi * r
    frac = max(0.0, min(1.0, (price - min_price) / (max_price - min_price)))
    offset = circumference * (1 - frac)
    price_fmt = f"Rp {price:,.0f}"

    return (
        f'<svg width="220" height="220" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="110" cy="110" r="{r}" fill="transparent" stroke="#1e293b" stroke-width="8"/>'
        f'<circle cx="110" cy="110" r="{r}" fill="transparent"'
        f' stroke="#00e5ff" stroke-width="12"'
        f' stroke-dasharray="{circumference:.1f}"'
        f' stroke-dashoffset="{offset:.1f}"'
        f' stroke-linecap="round"'
        f' transform="rotate(-90 110 110)"'
        f' style="filter:drop-shadow(0 0 8px rgba(0,229,255,0.7));"/>'
        f'<text x="110" y="100" text-anchor="middle"'
        f' font-family="JetBrains Mono,monospace" font-size="8" fill="#849396"'
        f' letter-spacing="2">ESTIMATED_PRICE</text>'
        f'<text x="110" y="124" text-anchor="middle"'
        f' font-family="Space Grotesk,sans-serif" font-size="15" font-weight="700"'
        f' fill="#00e5ff" style="filter:drop-shadow(0 0 10px rgba(0,229,255,0.5));">'
        f'{price_fmt}</text>'
        f'<text x="110" y="142" text-anchor="middle"'
        f' font-family="JetBrains Mono,monospace" font-size="8" fill="#00e5ff" opacity="0.6"'
        f' letter-spacing="1">CONFIDENCE: 94.2%</text>'
        f'</svg>'
    )


def render():
    pipeline = load_model()

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown("""
<div style="padding:1rem 0 0.5rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#00e5ff;
                letter-spacing:0.15em;margin-bottom:0.4rem;opacity:0.7;">
        PREDICTION_ENGINE // ENSEMBLE_V3
    </div>
    <h1 style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:28px;
               letter-spacing:-0.02em;color:#e5e2e1;margin:0 0 0.25rem;">PRICE_PREDICTOR</h1>
    <p style="font-family:'Inter',sans-serif;font-size:13px;color:#849396;margin:0;">
        Configure laptop specs and the ensemble model will synthesize a market valuation.
    </p>
</div>
""", unsafe_allow_html=True)

    if pipeline is None:
        st.markdown("""
<div style="background:rgba(147,0,10,0.15);border:1px solid rgba(255,180,171,0.3);
            border-radius:4px;padding:1rem;margin-bottom:1rem;">
    <div style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#ffb4ab;
                letter-spacing:0.1em;margin-bottom:0.4rem;">⚠ MODEL_NOT_FOUND</div>
    <p style="font-family:'Inter',sans-serif;font-size:13px;color:#ffdad6;margin:0;">
        Place your trained pipeline at
        <code style="background:rgba(255,255,255,0.1);padding:1px 5px;border-radius:3px;">laptop_pricer/model.pkl</code>
        and restart.
    </p>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ── Brand & Identity ──────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">BRAND &amp; IDENTITY</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([2, 2, 1, 1])
    with c1:
        brand = st.selectbox("Brand", ["Apple", "ASUS", "Dell", "HP", "Lenovo", "MSI",
                                        "Acer", "Samsung", "Razer", "Huawei", "Microsoft"], index=0, label_visibility="collapsed")
    with c2:
        model_name = st.selectbox("Model", ["Pro", "Air", "Ultra", "Gaming", "ZenBook",
                                                "ThinkPad", "XPS", "Spectre", "Blade",
                                                "MateBook", "Surface"], index=0, label_visibility="collapsed")
    with c3:
        in_stock = st.checkbox("In Stock", value=True)
    with c4:
        warranty_years = st.number_input("Warranty (yrs)", min_value=0, max_value=5, value=2, step=1)

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── CPU ───────────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">CPU</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([2, 2, 1, 3])
    with c1:
        cpu_brand = st.selectbox("CPU Brand", ["Intel", "AMD", "Apple"], index=0, label_visibility="collapsed")
    with c2:
        cpu_tier = st.selectbox("CPU Tier", ["Core i9", "Core i7", "Core i5", "Core i3",
                                                "Ryzen 9", "Ryzen 7", "Ryzen 5", "M4", "M3",
                                                "M2", "M1"], index=0, label_visibility="collapsed")
    with c3:
        cpu_gen = st.number_input("Gen", min_value=1, max_value=20, value=13, step=1)
    with c4:
        cpu_name = st.text_input("CPU Name", value="Intel Core i9-13620H",
                                    placeholder="e.g. Intel Core i9-13620H", label_visibility="collapsed")

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── GPU ───────────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">GPU</p>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        gpu_model = st.selectbox("GPU Model", ["RTX 5090", "RTX 5080", "RTX 5070", "RTX 5060",
                                                "RTX 4090", "RTX 4080", "RTX 4070", "RTX 4060",
                                                "RTX 3080", "RTX 3070", "RX 7900M",
                                                "Intel Arc", "Integrated"], index=2, label_visibility="collapsed")
    with c2:
        gpu_vram = st.selectbox("GPU VRAM", ["24GB", "16GB", "12GB", "8GB", "6GB", "4GB", "Shared"], index=3, label_visibility="collapsed")

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── RAM & Storage ─────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">MEMORY &amp; STORAGE</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        ram_gb = st.selectbox("RAM GB", [8, 16, 24, 32, 48, 64, 96, 128], index=3, label_visibility="collapsed")
    with c2:
        ram_type = st.selectbox("RAM Type", ["DDR5", "DDR4", "LPDDR5X", "LPDDR5",
                                                "LPDDR4X", "LPDDR4", "Unified"], index=0, label_visibility="collapsed")
    with c3:
        storage_gb = st.selectbox("Storage GB", [256, 512, 1000, 2000, 4000, 8000], index=3, label_visibility="collapsed")
    with c4:
        storage_type = st.selectbox("Storage Type", ["SSD", "NVMe", "HDD", "eMMC"], index=0, label_visibility="collapsed")

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── Display ───────────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">DISPLAY</p>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 2])
    with c1:
        display_size = st.number_input("Size\"", min_value=10.0, max_value=18.0,
                                        value=14.0, step=0.1, format="%.1f")
    with c2:
        display_type = st.selectbox("Panel", ["OLED", "Mini LED", "IPS", "TN",
                                                "AMOLED", "LCD"], index=0, label_visibility="collapsed")
    with c3:
        display_resolution = st.text_input("Resolution", value="2560x1600",
                                            placeholder="e.g. 2560x1600", label_visibility="collapsed")

    st.markdown('<hr style="border-color:rgba(0,229,255,0.08);margin:0.6rem 0;"/>', unsafe_allow_html=True)

    # ── OS & Physical ─────────────────────────────────────────────────────
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace;font-size:9px;color:#00e5ff;letter-spacing:0.12em;margin-bottom:0.4rem;">OS &amp; PHYSICAL</p>', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 3])
    with c1:
        os_version = st.selectbox("OS", ["Windows 11", "Windows 11 Pro", "Windows 10",
                                            "macOS", "Linux", "Chrome OS", "No OS"],
                                    index=0, label_visibility="collapsed")
    with c2:
        os_benefits = st.multiselect(
            "OS Benefits",
            ["Microsoft 365", "Office Home & Student", "Office Professional",
                "McAfee", "Norton", "Xbox Game Pass", "None"],
            default=["Microsoft 365", "Office Home & Student"],
            label_visibility="collapsed",
        )

    c1, c2 = st.columns(2)
    with c1:
        battery_wh = st.number_input("Battery (Wh)", min_value=20.0, max_value=200.0,
                                        value=60.0, step=1.0)
    with c2:
        weight_kg = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0,
                                    value=1.39, step=0.01, format="%.2f")

    st.markdown("<br/>", unsafe_allow_html=True)
    run = st.button("⚡  EXECUTE_PREDICTION", key="predict_btn", use_container_width=True)

    # ── Run prediction ────────────────────────────────────────────────────────
    predicted_price = None
    latency_ms = None

    if run:
        if pipeline is None:
            st.error("model.pkl not found — cannot run prediction.")
        else:
            user_input = {
                "in_stock":           in_stock,
                "brand":              brand,
                "model":              model_name,
                "ram_gb":             int(ram_gb),
                "ram_type":           ram_type,
                "storage_gb":         float(storage_gb),
                "storage_type":       storage_type,
                "display_size_inch":  float(display_size),
                "display_type":       display_type,
                "display_resolution": display_resolution,
                "battery_wh":         float(battery_wh),
                "weight_kg":          float(weight_kg),
                "os_version":         os_version,
                "os_benefits":        os_benefits if os_benefits else [],
                "gpu_model":          gpu_model,
                "gpu_vram":           gpu_vram,
                "cpu_name":           cpu_name,
                "warranty_years":     int(warranty_years),
                "cpu_brand":          cpu_brand,
                "cpu_tier":           cpu_tier,
                "cpu_gen":            int(cpu_gen),
            }
            df = pd.DataFrame([user_input])

            import cProfile, pstats, io

            # Pre-transform manually then predict — skip pipeline's pandas path
            pr = cProfile.Profile()
            pr.enable()
            t0 = time.perf_counter()
            predicted_price = pipeline.predict(df)[0]
            pr.disable()
            latency_ms = (time.perf_counter() - t0) * 1000

            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
            ps.print_stats(15)
            st.code(s.getvalue())

    # ── Summary banner ────────────────────────────────────────────────────────
    if predicted_price is not None:
        latency_color = "#00e5ff" if latency_ms < 100 else "#ff6b6b"
        st.markdown(f"""
<div style="padding:1rem 1.5rem;border-left:3px solid #00e5ff;
            background:rgba(0,229,255,0.04);border-radius:4px;margin-top:1rem;
            display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;">
    <div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#00e5ff;
                    letter-spacing:0.1em;margin-bottom:0.25rem;">PREDICTION_COMPLETE</div>
        <div style="display:flex;align-items:baseline;gap:0.5rem;flex-wrap:wrap;">
            <span style="font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:26px;color:#00e5ff;
                         text-shadow:0 0 20px rgba(0,229,255,0.4);">Rp {predicted_price:,.0f}</span>
            <span style="font-family:'JetBrains Mono',monospace;font-size:10px;color:#849396;">estimated market value</span>
        </div>
        <div style="margin-top:0.25rem;font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;">
            {brand} {model_name} · {cpu_tier} Gen{cpu_gen} · {gpu_model} · {ram_gb}GB {ram_type} · {int(storage_gb)}GB {storage_type} · {display_size}"
        </div>
    </div>
    <div style="text-align:right;">
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#3b494c;margin-bottom:2px;">INFERENCE_LATENCY</div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:700;color:{latency_color};">
            {latency_ms:.1f}<span style="font-size:11px;">ms</span>
        </div>
        <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:#3b494c;">
            {'✓ TARGET_MET' if latency_ms < 100 else '✗ OVER_BUDGET'}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    latency_str = f"{latency_ms:.1f}ms" if latency_ms is not None else "—"
    st.markdown(f"""
<div style="border-top:1px solid rgba(0,229,255,0.08);padding-top:1rem;
            display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
    <span style="font-family:'JetBrains Mono',monospace;font-weight:700;font-size:9px;color:#00e5ff;">
        © 2024 HARDWARE_ARCH_SYS | LATENCY: {latency_str}
    </span>
    <div style="display:flex;gap:1.5rem;">
        <span style="font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;">BS4_Scraper</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;">Ensemble_Core</span>
        <span style="font-family:'JetBrains Mono',monospace;font-size:9px;color:#3b494c;">Optuna_Log</span>
    </div>
</div>
""", unsafe_allow_html=True)