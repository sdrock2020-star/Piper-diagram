st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
        
        /* Hide top menu and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Make the header transparent instead of completely hidden so nothing breaks */
        [data-testid="stHeader"] { background-color: transparent; }

        /* NEW: Lock the sidebar by hiding the collapse button (Desktop only) */
        @media (min-width: 768px) {
            [data-testid="stSidebarCollapseButton"] { 
                display: none !important; 
            }
        }

        /* Existing Dashboard Card Styles */
        .dash-card {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.05);
            margin-bottom: 24px;
        }
        div[data-testid="metric-container"] {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.04);
            border-left: 5px solid #1f77b4;
        }
        .main-title { font-family: 'Segoe UI', sans-serif; font-weight: 800; color: #2c3e50; margin-bottom: 0px; padding-top: 10px; }
        .sub-title { color: #7f8c8d; font-size: 16px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)
