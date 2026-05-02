import streamlit as st


def render():
    # ── Hero ──────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding: 3rem 0 2rem;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#00e5ff;
                    letter-spacing:0.15em; margin-bottom:1rem; opacity:0.7;">
            NODE_ID: LPT-99X // SYSTEM ONLINE
        </div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:clamp(36px,5vw,56px);
                   line-height:1.05; letter-spacing:-0.03em; color:#e5e2e1; margin-bottom:1.5rem;">
            ALGORITHMIC <br/>
            PRICE <span style="background: linear-gradient(90deg, #00e5ff, #b0c6ff);
                               -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                               background-clip:text;">PREDICTION</span>
        </h1>
        <p style="font-family:'Inter',sans-serif; font-size:17px; line-height:1.7;
                  color:#bac9cc; max-width:600px; margin-bottom:2.5rem;">
            Solving market asymmetry through real-time scraping and ensemble-based regressive
            modeling. Transparent pricing for the hardware ecosystem.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        if st.button("🚀  RUN PREDICTOR", key="hero_predict"):
            st.session_state.page = "predictor"
            st.rerun()
    with col2:
        if st.button("📊  VIEW TECHNICALS", key="hero_tech"):
            st.session_state.page = "technicals"
            st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Bento stats row ───────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;
                letter-spacing:0.15em; margin-bottom:1rem;">// SYSTEM_METRICS</div>
    """, unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("ACCURACY_INDEX", "94.2%", delta="↑ 2.1%")
    with m2:
        st.metric("ENTRIES_SCRAPED", "1,204", delta="Live")
    with m3:
        st.metric("MODEL_MAE", "Rp 142K", delta="↓ optimized")
    with m4:
        st.metric("LATENCY", "14ms", delta="nominal")

    st.markdown("<br/>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Feature cards ─────────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3, gap="medium")

    with c1:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #00e5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; color:#00e5ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">visibility</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    Mission: Transparency
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc;">
                Laptop pricing is notoriously opaque. Retailers use dynamic pricing that fluctuates
                based on user cookies. This app normalizes market data and empowers consumers with
                raw, unbiased price assessments.
            </p>
            <div style="margin-top:auto; padding-top:1rem; border-top:1px solid rgba(0,229,255,0.1);
                        display:flex; justify-content:space-between; align-items:center;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">OBJECTIVE_01</span>
                <span class="material-symbols-outlined" style="color:#00e5ff; font-size:18px;">chevron_right</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; color:#b0c6ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">terminal</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    BS4 Data Ingestion
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc;">
                Using <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">BeautifulSoup4</span>,
                we scrape live inventory from 'Agres'. The pipeline processes thousands of DOM elements
                daily to extract CPU, GPU, RAM, and localized price indices.
            </p>
            <div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:1rem;">
                <span style="padding:2px 8px; background:#0f172a; border:1px solid rgba(0,229,255,0.3);
                             border-radius:3px; font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">#SCRAPER</span>
                <span style="padding:2px 8px; background:#0f172a; border:1px solid rgba(0,229,255,0.3);
                             border-radius:3px; font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">#PYTHON</span>
                <span style="padding:2px 8px; background:#0f172a; border:1px solid rgba(0,229,255,0.3);
                             border-radius:3px; font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">#AUTOMATION</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%; position:relative; overflow:hidden;">
            <div style="position:absolute; right:-2rem; top:-2rem; width:6rem; height:6rem;
                        background:rgba(0,229,255,0.05); border-radius:50%; filter:blur(20px);"></div>
            <div style="display:flex; align-items:center; gap:8px; color:#c3f5ff; margin-bottom:1rem;">
                <span class="material-symbols-outlined">neurology</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600;
                             font-size:11px; letter-spacing:0.1em; text-transform:uppercase;">
                    Ensemble Architecture
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1rem;">
                Multi-layered prediction engine combining XGBoost and Random Forest regressions.
                Hyperparameters optimized using <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">Optuna</span> to minimize MAE.
            </p>
            <div style="background:rgba(2,8,20,0.5); padding:0.75rem; border:1px solid rgba(0,229,255,0.2); border-radius:4px;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">ACCURACY_INDEX</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">94.2%</span>
                </div>
                <div style="background:#0f172a; height:4px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:94.2%; height:100%;
                                box-shadow:0 0 8px rgba(0,229,255,0.6);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/><br/>", unsafe_allow_html=True)

    # ── Infrastructure panel ──────────────────────────────────────────────────
    st.markdown("""
    <div class="glass-panel" style="padding:2.5rem;">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:3rem; align-items:start;">
            <div>
                <h2 style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:22px;
                           color:#e5e2e1; margin-bottom:1rem; letter-spacing:-0.01em;">
                    THE_INFRASTRUCTURE_REVEALED
                </h2>
                <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.7;
                          color:#bac9cc; margin-bottom:1.5rem;">
                    The back-end operates as a distributed system, handling asynchronous requests
                    to hardware distributors. Every data point is validated against historical
                    benchmarks to prevent outliers from skewing the prediction curve.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px;">
                    <li style="display:flex; align-items:center; gap:12px; color:#00e5ff; font-size:13px;">
                        <span class="material-symbols-outlined" style="font-size:16px;">check_circle</span>
                        <span style="font-family:'JetBrains Mono',monospace;">Latency-optimized web scraping engine</span>
                    </li>
                    <li style="display:flex; align-items:center; gap:12px; color:#00e5ff; font-size:13px;">
                        <span class="material-symbols-outlined" style="font-size:16px;">check_circle</span>
                        <span style="font-family:'JetBrains Mono',monospace;">Clean-room data normalization (JSON/CSV)</span>
                    </li>
                    <li style="display:flex; align-items:center; gap:12px; color:#00e5ff; font-size:13px;">
                        <span class="material-symbols-outlined" style="font-size:16px;">check_circle</span>
                        <span style="font-family:'JetBrains Mono',monospace;">Periodic model retraining via CRON jobs</span>
                    </li>
                </ul>
            </div>
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;
                        border-radius:4px; font-family:'JetBrains Mono',monospace; font-size:12px;
                        color:#67e8f9; position:relative; overflow:hidden;">
                <div style="position:absolute; top:0; left:0; right:0; height:2px;
                            background:rgba(0,229,255,0.08);"></div>
                <div style="display:flex; justify-content:space-between; border-bottom:1px solid rgba(0,229,255,0.15);
                            padding-bottom:8px; margin-bottom:12px;">
                    <span>terminal — ensemble_log — 80x24</span>
                    <div style="display:flex; gap:6px; align-items:center;">
                        <div style="width:8px; height:8px; border-radius:50%; background:rgba(239,68,68,0.5);"></div>
                        <div style="width:8px; height:8px; border-radius:50%; background:rgba(234,179,8,0.5);"></div>
                        <div style="width:8px; height:8px; border-radius:50%; background:rgba(34,197,94,0.5);"></div>
                    </div>
                </div>
                <p style="opacity:0.7; margin-bottom:4px;">[INFO] Loading Scraper Core...</p>
                <p style="opacity:0.7; margin-bottom:4px;">[SUCCESS] Scraped 1204 entries from 'agres'</p>
                <p style="opacity:0.7; margin-bottom:4px;">[PROCESS] Normalizing column 'price_ron'</p>
                <p style="color:#c3f5ff; margin-bottom:4px;">&gt; Training XGBoost v1.4.2...</p>
                <p style="color:#c3f5ff; margin-bottom:12px;">&gt; Current MAE: 142.023</p>
                <p style="opacity:0.7;">[INFO] Pushing weights to production_edge</p>
                <p style="margin-top:12px; color:#00e5ff;">_</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border-top:1px solid rgba(0,229,255,0.1); padding-top:1.5rem;
                display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <span style="font-family:'JetBrains Mono',monospace; font-weight:700; font-size:10px; color:#00e5ff;">
            © 2024 HARDWARE_ARCH_SYS | LATENCY: 14ms
        </span>
        <div style="display:flex; gap:2rem;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">BS4_Scraper</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Ensemble_Core</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Optuna_Log</span>
        </div>
    </div>
    """, unsafe_allow_html=True)