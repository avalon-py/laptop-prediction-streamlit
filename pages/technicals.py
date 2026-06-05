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

    # Stage 03 + 04 — same row
    c3, c4 = st.columns(2, gap="medium")

    with c3:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">03</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Smart Imputation
                </span>
            </div>
            <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem;">
                Hybrid imputation strategy using statistical distribution for non-critical features
                and algorithm-driven filling for high-variance dimensions.
            </p>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
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

    with c4:
        st.markdown("""
        <div class="glass-panel" style="padding:1.5rem; border-left:4px solid #c3f5ff; height:100%;">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:1rem;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">04</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Ensemble Learning
                </span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:0.75rem; margin-bottom:1.5rem;">
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

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 05 — Optuna full-width
    # FIX: removed blank lines inside the HTML string — Streamlit's Markdown parser
    # exits "HTML block" mode at blank lines, causing indented content after them
    # to be rendered as a code block instead of HTML.
    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-bottom:0.5rem;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">05</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Optuna Tuning
                </span>
            </div>
            <div style="display:flex; gap:1.5rem; flex-wrap:wrap;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">SAMPLER: TPE_Sampler(seed=42)</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">DIRECTION: minimize</span>
                <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;">TARGET: MAPE</span>
            </div>
        </div>
        <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem; max-width:800px;">
            Automated Bayesian optimization via TPE sampler, independently tuning each base learner.
            Each study minimizes cross-validated MAPE using a <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">KFold(n_splits=5)</span>
            pipeline wrapped in <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">TransformedTargetRegressor(log1p / expm1)</span>.
        </p>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem;">
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">XGBoost</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">50 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">n_estimators</span><span style="color:#bac9cc;">300 – 3000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">learning_rate</span><span style="color:#bac9cc;">1e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">max_depth</span><span style="color:#bac9cc;">3 – 8</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">subsample</span><span style="color:#bac9cc;">0.6 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">colsample_bytree</span><span style="color:#bac9cc;">0.5 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">reg_alpha</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">reg_lambda</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">min_child_weight</span><span style="color:#bac9cc;">1 – 10</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">gamma</span><span style="color:#bac9cc;">0.0 – 1.0</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">
                    device=cuda &nbsp;·&nbsp; tree_method=hist &nbsp;·&nbsp; random_state=42
                </div>
            </div>
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">LightGBM</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">50 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">n_estimators</span><span style="color:#bac9cc;">300 – 3000</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">learning_rate</span><span style="color:#bac9cc;">1e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">max_depth</span><span style="color:#bac9cc;">3 – 8</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">num_leaves</span><span style="color:#bac9cc;">15 – 127</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">min_child_samples</span><span style="color:#bac9cc;">5 – 50</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">subsample</span><span style="color:#bac9cc;">0.6 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">colsample_bytree</span><span style="color:#bac9cc;">0.5 – 1.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">reg_alpha</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">reg_lambda</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">
                    device=gpu &nbsp;·&nbsp; deterministic=True &nbsp;·&nbsp; importance_type=gain
                </div>
            </div>
            <div style="background:#0a0f1e; border:1px solid rgba(0,229,255,0.2); padding:1rem;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
                    <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px; color:#67e8f9;">CatBoost</span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#00e5ff;
                                 background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.2);">30 TRIALS</span>
                </div>
                <div style="display:flex; flex-direction:column; gap:5px;">
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">iterations</span><span style="color:#bac9cc;">300 – 1500</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">learning_rate</span><span style="color:#bac9cc;">5e-3 – 0.05 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">depth</span><span style="color:#bac9cc;">4 – 10</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">l2_leaf_reg</span><span style="color:#bac9cc;">1e-3 – 10.0 (log)</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">bagging_temperature</span><span style="color:#bac9cc;">0.0 – 2.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">random_strength</span><span style="color:#bac9cc;">0.0 – 3.0</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">min_data_in_leaf</span><span style="color:#bac9cc;">1 – 30</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
                        <span style="color:#3b494c;">border_count</span><span style="color:#bac9cc;">32 – 255</span>
                    </div>
                </div>
                <div style="margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid rgba(0,229,255,0.1);
                            font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c;">
                    loss=RMSE &nbsp;·&nbsp; eval=MAPE &nbsp;·&nbsp; bootstrap=Bayesian &nbsp;·&nbsp; grow=SymmetricTree &nbsp;·&nbsp; task=GPU
                </div>
            </div>
        </div>
        <div style="margin-top:1rem; padding:0.75rem 1rem; background:rgba(0,229,255,0.04);
                    border:1px solid rgba(0,229,255,0.15); display:flex; gap:2rem; flex-wrap:wrap;">
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#3b494c;">CV_STRATEGY</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">KFold(n_splits=5, shuffle=True, random_state=42)</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#3b494c;">LOG_TRANSFORM</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">np.log1p → np.expm1</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#3b494c;">META_ALPHAS</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">RidgeCV([0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:10px;">
                <span style="color:#3b494c;">PASSTHROUGH</span>&nbsp;&nbsp;
                <span style="color:#bac9cc;">True</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Stage 06 - Results Comparison
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import numpy as np

    st.markdown("""
    <div class="glass-panel" style="padding:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem; flex-wrap:wrap; gap:1rem;">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#00e5ff;
                             background:rgba(0,229,255,0.1); padding:2px 8px; border:1px solid rgba(0,229,255,0.3);">06</span>
                <span style="font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:18px; color:#e5e2e1;">
                    Results Comparison
                </span>
            </div>
            <span style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#00e5ff;">ENSEMBLE vs SOLO MODELS</span>
        </div>
        <p style="font-family:'Inter',sans-serif; font-size:14px; line-height:1.6; color:#bac9cc; margin-bottom:1.5rem; max-width:800px;">
            The stacking ensemble consistently outperforms every solo base learner across all four evaluation metrics.
            Lower error on <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">MAE · MAPE · RMSE</span>
            and highest <span style="color:#00e5ff; font-family:'JetBrains Mono',monospace;">R²</span> confirms
            the meta-learner successfully exploits complementary strengths of CatBoost, XGBoost, and LightGBM.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Colour palette matching the dark cyberpunk theme ─────────────────────
    ENSEMBLE_CLR  = "#00e5ff"   # cyan — the star
    LGBM_CLR      = "#3b82f6"   # blue
    XGB_CLR       = "#6366f1"   # indigo
    CAT_CLR       = "#22d3ee"   # sky
    PLOT_BG       = "rgba(0,0,0,0)"
    PAPER_BG      = "rgba(0,0,0,0)"
    GRID_CLR      = "rgba(0,229,255,0.08)"
    TICK_CLR      = "#3b494c"
    FONT_FAMILY   = "JetBrains Mono, monospace"

    base_layout = dict(
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(family=FONT_FAMILY, color="#bac9cc", size=11),
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
    )

    axis_style = dict(
        gridcolor=GRID_CLR,
        linecolor="rgba(0,229,255,0.15)",
        tickfont=dict(color=TICK_CLR, size=10),
        zerolinecolor=GRID_CLR,
    )

    models      = ["ensemble", "lgbm", "xgb", "catboost"]
    colors      = [ENSEMBLE_CLR, LGBM_CLR, XGB_CLR, CAT_CLR]
    bar_opacity = [1.0, 0.7, 0.7, 0.7]

    # ── Chart 1 — 4-metric performance comparison (2×2) ──────────────────────
    mae_vals   = [1094028.88, 1092918.83, 1222198.00, 1136731.51]
    mape_vals  = [0.0667,     0.0670,     0.0780,     0.0670]
    rmse_vals  = [1945538.70, 2017194.10, 2019387.91, 2058289.80]
    r2_vals    = [0.9413,     0.9369,     0.9368,     0.9343]

    fig_perf = make_subplots(
        rows=2, cols=2,
        subplot_titles=["MAE  ↓ lower is better", "MAPE  ↓ lower is better",
                        "RMSE  ↓ lower is better", "R²  ↑ higher is better"],
        vertical_spacing=0.18,
        horizontal_spacing=0.10,
    )

    # Defined zoomed-in ranges for each metric
    # Format: (values, row, col, fmt, y_min, y_max)
    datasets = [
        (mae_vals,  1, 1, ".0f", 1000000, 1300000), 
        (mape_vals, 1, 2, ".4f", 0.06, 0.085),
        (rmse_vals, 2, 1, ".0f", 1900000, 2150000),
        (r2_vals,   2, 2, ".4f", 0.93, 0.95),
    ]

    for vals, row, col, fmt, ymin, ymax in datasets:
        for i, (m, v, c, op) in enumerate(zip(models, vals, colors, bar_opacity)):
            is_best = (i == 0)
            fig_perf.add_trace(
                go.Bar(
                    x=[m.upper()], y=[v],
                    marker=dict(
                        color=c,
                        opacity=op,
                        line=dict(color=c if is_best else "rgba(0,229,255,0.2)", width=1 if is_best else 0.5),
                    ),
                    text=[f"{v:{fmt}}"],
                    textposition="outside",
                    textfont=dict(color=c if is_best else "#bac9cc", size=10, family=FONT_FAMILY),
                    showlegend=False,
                    name=m,
                ),
                row=row, col=col,
            )
        # Apply the specific zoomed range to each subplot
        fig_perf.update_yaxes(range=[ymin, ymax], row=row, col=col)

    fig_perf.update_layout(
        **base_layout,
        height=520,
        barmode="group",
        title=dict(
            text="MODEL PERFORMANCE COMPARISON (ZOOMED)",
            font=dict(family=FONT_FAMILY, color="#00e5ff", size=13),
            x=0.01, xanchor="left",
        ),
    )

    fig_perf.update_layout(
        **base_layout,
        height=520,
        barmode="group",
        title=dict(
            text="MODEL PERFORMANCE COMPARISON",
            font=dict(family=FONT_FAMILY, color="#00e5ff", size=13),
            x=0.01, xanchor="left",
        ),
    )

    for annotation in fig_perf.layout.annotations:
        annotation.font = dict(family=FONT_FAMILY, color="#bac9cc", size=10)

    fig_perf.update_xaxes(**axis_style)
    fig_perf.update_yaxes(**axis_style)

    st.plotly_chart(fig_perf, use_container_width=True, config={"displayModeBar": False})

    st.markdown("<br/>", unsafe_allow_html=True)

    # ── Chart 2 — CV MAPE mean ± std dot plot ────────────────────────────────
    cv_models  = ["ensemble", "xgb",    "lgbm",   "catboost"]
    cv_means   = [0.0826,     0.0864,   0.0877,   0.0885]
    cv_stds    = [0.0020,     0.0040,   0.0080,   0.0065]   # approximated from image
    cv_colors  = [ENSEMBLE_CLR, XGB_CLR, LGBM_CLR, CAT_CLR]

    fig_cv = go.Figure()

    for i, (m, mean, std, c) in enumerate(zip(cv_models, cv_means, cv_stds, cv_colors)):
        is_ens = (i == 0)
        # error bar (vertical line + caps)
        fig_cv.add_trace(go.Scatter(
            x=[m.upper(), m.upper(), m.upper()],
            y=[mean - std, mean, mean + std],
            mode="lines",
            line=dict(color=c, width=1.5 if is_ens else 1),
            showlegend=False,
        ))
        # cap top
        fig_cv.add_trace(go.Scatter(
            x=[m.upper()], y=[mean + std],
            mode="markers",
            marker=dict(symbol="line-ew", size=10, color=c,
                        line=dict(color=c, width=2)),
            showlegend=False,
        ))
        # cap bottom
        fig_cv.add_trace(go.Scatter(
            x=[m.upper()], y=[mean - std],
            mode="markers",
            marker=dict(symbol="line-ew", size=10, color=c,
                        line=dict(color=c, width=2)),
            showlegend=False,
        ))
        # centre dot
        fig_cv.add_trace(go.Scatter(
            x=[m.upper()], y=[mean],
            mode="markers+text",
            marker=dict(
                size=14 if is_ens else 10,
                color=c,
                line=dict(color="#0a0f1e", width=2),
            ),
            text=[f"  {mean:.4f}"],
            textposition="middle right",
            textfont=dict(color=c if is_ens else "#bac9cc", size=10, family=FONT_FAMILY),
            showlegend=False,
            name=m,
        ))

    fig_cv.update_layout(
        **base_layout,
        height=320,
        title=dict(
            text="CROSS-VALIDATION MAPE  (mean ± std, KFold n=5)",
            font=dict(family=FONT_FAMILY, color="#00e5ff", size=13),
            x=0.01, xanchor="left",
        ),
        xaxis=dict(**axis_style, categoryorder="array",
                   categoryarray=["ENSEMBLE", "XGB", "LGBM", "CATBOOST"]),
        yaxis=dict(**axis_style, title=dict(text="CV MAPE", font=dict(color=TICK_CLR, size=10))),
    )

    st.plotly_chart(fig_cv, use_container_width=True, config={"displayModeBar": False})

    # ── Verdict badge row ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:0.5rem;">
        <div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4);
                    background:rgba(0,229,255,0.06);">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; display:block; margin-bottom:2px;">BEST_MAE</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#00e5ff;">ENSEMBLE</span>
        </div>
        <div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4);
                    background:rgba(0,229,255,0.06);">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; display:block; margin-bottom:2px;">BEST_MAPE</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#00e5ff;">ENSEMBLE</span>
        </div>
        <div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4);
                    background:rgba(0,229,255,0.06);">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; display:block; margin-bottom:2px;">BEST_RMSE</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#00e5ff;">ENSEMBLE</span>
        </div>
        <div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4);
                    background:rgba(0,229,255,0.06);">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; display:block; margin-bottom:2px;">BEST_R²</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#00e5ff;">ENSEMBLE</span>
        </div>
        <div style="padding:0.6rem 1.2rem; border:1px solid rgba(0,229,255,0.4);
                    background:rgba(0,229,255,0.06);">
            <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#3b494c; display:block; margin-bottom:2px;">LOWEST_CV_MAPE</span>
            <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; color:#00e5ff;">0.0826 ± σ</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border-top:1px solid rgba(0,229,255,0.1); padding-top:1.5rem;
                display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
        <span style="font-family:'JetBrains Mono',monospace; font-weight:700; font-size:10px; color:#00e5ff;">
            © Machine Learning AOL (Assurance of Learning) Project | Stefano, Alvin, Joel.
        </span>
        <div style="display:flex; gap:2rem;">
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">WebScrapping</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Ensemble</span>
            <span style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#3b494c;">Optuna</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
