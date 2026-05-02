import streamlit as st


def render():
    st.markdown("""
    <div style="padding: 2rem 0 1.5rem;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                    letter-spacing:0.15em; margin-bottom:0.75rem; opacity:0.7;">PIPELINE_ARCHITECTURE // V3.2.1</div>
        <h1 style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:38px;
                   letter-spacing:-0.02em; color:#e5e2e1; margin-bottom:0.5rem;">
            TECHNICAL_DEEP_DIVE
        </h1>
        <p style="font-family:'Inter',sans-serif; font-size:15px; color:#bac9cc; max-width:600px;">
            Six-stage ML pipeline from raw DOM scraping to validated ensemble predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 01 + 02
    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #00e5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">01</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Web Scraping
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Asynchronous scraper built with <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">BeautifulSoup4</span>
                + <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">httpx</span>.
                Extracts structured laptop data from 'Agres' marketplace with rate-limiting and retry logic.
            </p>
            <div>
                <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace;
                            font-size:9px; color:#00e5ff; margin-bottom:4px;">
                    <span>COLLECTION_RATE</span><span>98.7%</span>
                </div>
                <div style="background:#0f172a; height:3px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:98.7%; height:100%; box-shadow:0 0 6px rgba(0,229,255,0.5);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">02</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Data Normalization
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Manual remap of ambiguous product strings. Normalization of SKU variants across
                multiple vendor formats using a canonical hardware taxonomy.
            </p>
            <div>
                <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace;
                            font-size:9px; color:#00e5ff; margin-bottom:4px;">
                    <span>REMAP_ACCURACY</span><span>92.4%</span>
                </div>
                <div style="background:#0f172a; height:3px; border-radius:2px; overflow:hidden;">
                    <div style="background:#00e5ff; width:92.4%; height:100%; box-shadow:0 0 6px rgba(0,229,255,0.5);"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 03 - Imputation
    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                         background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">03</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                Smart Imputation
            </span>
        </div>
        <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem; max-width:600px;">
            Hybrid imputation strategy using statistical distribution for non-critical features
            and algorithm-driven filling for high-variance dimensions.
        </p>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; max-width:400px;">
            <div style="padding:1rem; border:1px solid rgba(0,229,255,0.2); background:rgba(0,229,255,0.05);">
                <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff; margin-bottom:4px;">GENERAL</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:20px; color:#e5e2e1;">MEDIAN</div>
            </div>
            <div style="padding:1rem; border:1px solid rgba(0,104,237,0.2); background:rgba(0,104,237,0.05);">
                <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#b0c6ff; margin-bottom:4px;">WEIGHT_KG</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:20px; color:#e5e2e1;">KNN_K7</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 04 + 05
    c3, c4 = st.columns([7, 5], gap="medium")

    with c3:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #c3f5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">04</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Ensemble Learning
                </span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:1.5rem;">
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; margin-bottom:4px;">BASE_01</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">CatBoost</div>
                </div>
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; margin-bottom:4px;">BASE_02</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">XGBoost</div>
                </div>
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; margin-bottom:4px;">BASE_03</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">RandomForest</div>
                </div>
                <div class="glass-panel" style="padding:0.75rem; border-color:rgba(0,229,255,0.1);">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; margin-bottom:4px;">BASE_04</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#67e8f9;">LightGBM</div>
                </div>
            </div>
            <div style="background:rgba(0,229,255,0.08); padding:1rem; border:1px solid rgba(0,229,255,0.3);
                        border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff; opacity:0.6; margin-bottom:4px;">META_LEARNER</div>
                    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:22px; color:#c3f5ff;">RIDGECV</div>
                </div>
                <span class="material-symbols-outlined" style="color:#00e5ff; font-size:2rem;">account_tree</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">05</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Optuna Tuning
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Automated Bayesian optimization for hyperparameter searching. Navigating the
                N-dimensional space to find global minima.
            </p>
            <div style="display:flex; flex-direction:column; gap:10px;">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff; flex-shrink:0;"></div>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#d1d5db;">TRIAL_SET: 1,000 iterations</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff; flex-shrink:0;"></div>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#d1d5db;">SAMPLER: TPE_Sampler</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="width:8px; height:8px; border-radius:50%; background:#00e5ff; box-shadow:0 0 8px #00e5ff; flex-shrink:0;"></div>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#d1d5db;">PRUNER: MedianPruner</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 06 - Validation
    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; flex-wrap:wrap; gap:1rem;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">06</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Validation Protocol
                </span>
            </div>
            <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#00e5ff;">METHOD: STRATIFIED_BINNING_KFOLD</span>
        </div>
        <div style="display:grid; grid-template-columns:repeat(5,1fr); gap:12px;">
    """, unsafe_allow_html=True)

    folds = [("FOLD_01", "0.942"), ("FOLD_02", "0.938"), ("FOLD_03", "0.951"), ("FOLD_04", "0.944"), ("FOLD_05", "0.947")]
    fold_html = ""
    for label, val in folds:
        fold_html += f"""
        <div style="height:6rem; background:#0a0f1e; border:1px solid rgba(0,229,255,0.2);
                    display:flex; flex-direction:column; align-items:center; justify-content:center;
                    gap:6px;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">{label}</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:22px; color:#00e5ff;">{val}</span>
        </div>
        """

    st.markdown(fold_html + "</div></div>", unsafe_allow_html=True)

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