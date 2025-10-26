# app.py - "ETL of Me" interactive Streamlit app
import streamlit as st
import pandas as pd
import time
import plotly.express as px

# ---------- THEME / BRAND ----------
SIEMENS_GREEN = "#009a38"   # SH Green from UI MarCom
ACCENT = SIEMENS_GREEN

st.set_page_config(page_title="ETL of Khurshid", layout="wide", page_icon="🧭")

# ---------- STYLING ----------
st.markdown(f"""
    <style>
    .stApp {{ font-family: "Inter", sans-serif; }}
    .big-button {{
        background-color: {ACCENT};
        color: white;
        padding: 12px 18px;
        border-radius: 8px;
        font-weight: 600;
        font-size:18px;
        text-align:center;
    }}
    .card {{ padding:14px; border-radius:10px; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }}
    .muted {{ color: #666; font-size: 14px; }}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER / LANDING ----------
col1, col2 = st.columns([3,1])
with col1:
    st.title("ETL of Khurshid — an interactive story")
    # st.write("Click **Start** and pick something the room cares about — then let's walk through it together.")
with col2:
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/khurshid-uktamov/" target="_blank">
            <img src="https://media.licdn.com/dms/image/D4D03AQG4LKb2hHq_KA/profile-displayphoto-shrink_400_400/0/1688210112345?e=2147483647&v=beta&t=example" width="120" alt="Khurshid Uktamov">
        </a>
        """,
        unsafe_allow_html=True
    )

# ---------- INTERVIEWER CHOICE ----------
st.markdown("---")

st.subheader("Quick ice-breaker — click one of my hobbies!")

col1, col2, col3, col4 = st.columns(4)

if col1.button("⚽ Football", key="ib_football"):
    st.success("Teamwork, strategy, and performance analysis — football taught me how data reveals winning patterns, "
               "just like analyzing supply-chain KPIs.")

if col2.button("🈶 Japanese Culture", key="ib_japanese"):
    st.success("Learning Japanese strengthened my discipline and attention to detail — the same mindset I use "
               "when writing clean, documented SQL and Python for scalable apps.")

if col3.button("💪 Discipline / Gym", key="ib_gym"):
    st.success("Consistency and measurement drive progress in the gym — exactly how I iterate ETL performance, "
               "monitor data quality, and improve efficiency week by week.")

if col4.button("🏓 Table Tennis", key="ib_tt"):
    st.success("In table tennis, you must react to fast changes — it trained me to stay alert, "
               "respond quickly when systems fail, and adapt under pressure — essential for data operations and incident handling.")



# ---------- NAVIGATION ----------
st.markdown("---")
if 'step' not in st.session_state:
    st.session_state.step = "landing"

def go(step):
    st.session_state.step = step

if st.session_state.step == "landing":
    st.markdown("""
        <div class="card">
        <h3>Start the ETL</h3>
        <p class="muted">We'll move through Extract → Transform → Load → Dashboard. Use the Next button or click a step below.</p>
        </div>
    """, unsafe_allow_html=True)
    cols = st.columns(4)
    steps = ["Extract","Transform","Load","Dashboard"]
    for i,s in enumerate(steps):
        if cols[i].button(s):
            go(s.lower())
    st.markdown("<div style='margin-top:12px'></div>", unsafe_allow_html=True)
    if st.button("Start ETL", key="start"):
        go("extract")

# ---------- EXTRACT ----------
if st.session_state.step == "extract":
    st.header("1) Extract — From small town of Uzbekistan moving to capital Tashkent for better education opportunities.")
    
    colA, colB = st.columns([2,1])
    with colA:
        st.markdown("""
        - 🎓 **Studies in Power Engineering and audit** — taught me how systems behave and how small inefficiencies can cascade.
        - 💼 **Early Career Shift to Data** — learned Python & SQL.
        - 🚀 **Helping a Startup Optimize Its CRM Funnel** — analyzed customer journey data, identified drop-off points, 
          and proposed targeted follow-ups that increased qualified leads.
        """)
        st.caption("These experiences gave me diverse raw inputs — technical, analytical, and business-oriented.")
    with colB:
        st.metric("Raw Datasets Analyzed", "50+")
        st.metric("Data Volume", "10M+ rows")
    
    st.markdown("---")
    if st.button("Next → Transform", key="next_transform"):
        go("transform")
    if st.button("Back to start", key="back_extract"):
        go("landing")



# ---------- TRANSFORM ----------
if st.session_state.step == "transform":
    st.header("2) Transform — This is where I came to Poland and leveled up!")
    st.markdown("""
        - Joined NielsenIQ, honed my Python and SQL skills working on retail data.
        - Sleepless nights attending bootcamps for data engineering and analytics.
        - Designing Different Data Models and Data Warehouses.
    """)
    st.subheader("Mini dashboard to showcase my impact with Python automation: before vs after")
    before = dict(tasks=30, hours=10)
    after = dict(tasks=30, hours=2)
    fig = px.bar(x=["Before","After"], y=[before["hours"], after["hours"]], labels={"x":"State","y":"Hours/week"})
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Example: automation cut weekly manual time from 10h to 2h for recurring reports.")
    st.markdown("**Show me a tiny automation snippet**")
    if st.checkbox("Show code"):
        st.code("""# example: tidy_sales.py
import pandas as pd
def tidy_sales(df):
    df = df.assign(date=pd.to_datetime(df['date']))
    df = df.groupby(['product','date']).sum().reset_index()
    return df
""", language="python")
    st.markdown("---")
    if st.button("Next → Load", key="next_load"):
        go("load")
    if st.button("Back", key="back_transform"):
        go("extract")


# ---------- LOAD ----------
if st.session_state.step == "load":
    st.header("3) Load — it is where my data engineering shines")
    st.write("Scalable Data Architecture & Enterprise Impact, data models, and performance optimization — the foundation of reliable analytics.")

    # Columns for layout
    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.markdown(
            """
            <h3>🎮 <a href="https://dbdiagram.io/d/WoT-World-of-Tanks-68893724cca18e685c5434a6" target="_blank" style="color:#009a38; text-decoration:none;">World of Tanks — Battle/Player Data Warehouse</a></h3>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
        **Scale:** 18M battles/day → 270M player rows/day  
        **Design:** Snowflake Schema, SCD Type 2, Monthly Partitioning  
        **Impact:** ↓ 90% + storage (324B → 32.4M rows/year)  
        **Focus:** Performance, History Preservation, Lifecycle Automation  

        ---
                    

        ### 🏅 Olympics’ History — Data Engineering & Visualization
        **Scope:** 126 years of data → 154,000+ athletes  
        **Tech:** Azure Data Lake, Databricks, Synapse, PySpark  
        **Impact:** Cloud-based analytics dashboards covering 235 countries  
        **Links:** 
        [GitHub](https://github.com/khurshiduktamov/Olympic-Analytics-Engineering) | 
        [Tableau](https://public.tableau.com/app/profile/khurshid.uktamov/viz/OlympicDataAnalyticsProject/Home)
        
        ---
                    
        ### 🏪 NielsenIQ — Retail ETL & Governance
        **Tools:** Python (Pandas, SQLAlchemy), SQL, Parquet/CSV, Power BI  
        **Improvements:**  
        - ↓ 94% project delivery time (7 days → 4 hours)  
        - ↑ 95%+ data accuracy  
        - ↓ 60% onboarding time  (12 weeks → 5 weeks)  
        **Focus:** DataOps, SLA Compliance, Governance Framework  
        """)

    with col2:
        # st.image("https://via.placeholder.com/450x300.png?text=Data+Pipeline+Diagram", caption="ETL Architecture (Simplified)")
        st.metric("Daily Rows Processed", "270M+")
        st.metric("Accuracy", "95%+")
        st.metric("Global Coverage", "235 Countries")

    st.markdown("---")
    if st.button("Next → Dashboard", key="next_dashboard"):
        go("dashboard")
    if st.button("Back", key="back_load"):
        go("transform")


# ---------- DASHBOARD ----------
if st.session_state.step == "dashboard":
    st.header("4) Skills & Values — My fit at Siemens Healthineers")
    st.write("Here’s how my skills, experience, and mindset match your requirements and values.")

    # Bubble chart: Technical Skills vs JD Needs
    import plotly.express as px
    df_skills = pd.DataFrame({
        "Skill":["Python","SQL","ETL","Data Modeling","Cloud (Azure)","Tableau","PowerBI","PySpark"],
        "JD_Requirement":["Programming","Database","ETL","Data Architecture","Cloud","Visualization","Visualization","Big Data"],
        "Experience_Years":[4,4,3,3,1,1,2,1]
    })

    # color_continuous_scale: low -> high. Use lighter green for less experience, darker (SIEMENS_GREEN) for more.
    fig = px.scatter(df_skills, x="Skill", y="JD_Requirement",
                     size="Experience_Years", color="Experience_Years",
                     color_continuous_scale=["#66cc99", SIEMENS_GREEN],
                     size_max=50, text="Skill", title="Technical Skills vs JD Requirements")
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    # Soft skills cards — displayed in two rows (3 + 2)
    st.subheader("Interpersonal & Professional Skills")
    # First row: 3 items
    r1c1, r1c2, r1c3 = st.columns(3)
    r1c1.metric("Analytical Mind", "✅ Experienced")
    r1c2.metric("Proactive", "✅ Always")
    r1c3.metric("Team Collaboration", "✅ Cross-functional")
    # Second row: 2 items
    r2c1, r2c2 = st.columns(2)
    r2c1.metric("Adaptability", "✅ Fast Learner")
    r2c2.metric("Communication", "✅ Fluent English / Intl Teams")

    st.markdown("---")
    
    import plotly.express as px
    import pandas as pd

    # Define the matrix
    data = pd.DataFrame({
        "Trait / Personality": ["Proactive","Analytical Mind","Adaptable","Team Collaboration","Curious / Fast Learner"],
        "Innovation":[9,10,8,7,9],
        "Patient / Impact":[7,8,9,8,7],
        "Collaboration":[8,7,8,10,7],
        "Continuous Learning":[9,8,9,7,10]
    })

    # Melt the dataframe for plotly
    df_melt = data.melt(id_vars="Trait / Personality", var_name="Siemens Value", value_name="Alignment")

    # Create heatmap
    fig = px.density_heatmap(
        df_melt,
        x="Siemens Value",
        y="Trait / Personality",
        z="Alignment",
        color_continuous_scale="Greens",
        text_auto=True
    )

    fig.update_layout(
        title="Alignment of My Personality with Siemens Healthineers Values as a Heatmap",
        xaxis_title="Siemens Values",
        yaxis_title="My Traits / Personality",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.markdown("---")
    if st.button("Restart Journey", key="restart"):
        go("landing")


# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built live for this interview • Khurshid — where data meets design, and design meets purpose.")
