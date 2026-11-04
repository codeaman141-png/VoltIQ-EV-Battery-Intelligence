import os
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="VoltIQ | EV Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DESIGN COLOURS ----------------
BG = "#080D16"
PANEL = "#101A2A"
BLUE = "#438BFF"
CYAN = "#48DDF2"
RED = "#FF5364"
WHITE = "#F3F6FC"
MUTED = "#AAB8CC"

# ---------------- CUSTOM CSS ----------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {{
    background: linear-gradient(145deg,#080D16,#0A1424,#080D16);
    color: {WHITE};
    font-family: 'DM Sans', sans-serif;
}}

header[data-testid="stHeader"] {{
    background: #080D16 !important;
    border-bottom: 1px solid #263B57;
}}

[data-testid="stDecoration"] {{
    background: linear-gradient(90deg,{BLUE},{CYAN}) !important;
}}

.block-container {{
    max-width: 1530px;
    padding: 1.5rem 2rem 3rem;
}}

[data-testid="stSidebar"] {{
    background: linear-gradient(180deg,#0D1727,#09111E);
    border-right: 1px solid #263B57;
}}

[data-testid="stSidebar"] * {{
    color: #E7EDF7;
}}

h1,h2,h3,h4 {{
    color: {WHITE} !important;
    font-family: 'Manrope', sans-serif !important;
}}

p,label {{
    color: {MUTED};
}}

.stCaption, [data-testid="stCaptionContainer"] p {{
    font-size: 15px !important;
    line-height: 1.6 !important;
    color: #B8C7DA !important;
}}

[data-testid="stSidebar"] label {{
    font-size: 15px !important;
}}

[data-testid="stSidebar"] [data-baseweb="input"] > div,
[data-testid="stSidebar"] [data-baseweb="select"] > div,
[data-testid="stSidebar"] input {{
    background: #142238 !important;
    color: white !important;
    border-color: #2A3C56 !important;
}}

[data-testid="stSlider"] [role="slider"] {{
    background: {BLUE} !important;
}}

.eyebrow {{
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
    color: {CYAN};
    text-transform: uppercase;
}}

.muted {{
    font-size: 17px;
    color: #B8C7DA;
    line-height: 1.6;
}}

.kicker {{
    font-size: 15px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #AABBD1;
    margin-bottom: 10px;
}}

.hero {{
    background: linear-gradient(115deg,#132741,#0C1727,#122C48);
    border: 1px solid #263C59;
    border-radius: 23px;
    padding: 27px 30px;
    min-height: 245px;
}}

.hero-title {{
    font-family: 'Manrope';
    font-size: clamp(30px,4vw,48px);
    font-weight: 800;
    line-height: 1.1;
    color: #F5F8FF;
    margin: 12px 0;
}}

.hero-copy {{
    color: #B8C7DA;
    font-size: 15px;
    line-height: 1.7;
}}

.hero-stat {{
    margin-top: 22px;
    display: flex;
    gap: 28px;
    flex-wrap: wrap;
}}

.hero-stat b {{
    display: block;
    color: white;
    font-size: 22px;
}}

.hero-stat span {{
    font-size: 13px;
    color: #B8C7DA;
    font-weight: 700;
}}

.metric-card {{
    background: linear-gradient(145deg,#14243B,#0F1929);
    border: 1px solid #263B57;
    border-radius: 16px;
    padding: 19px;
    min-height: 120px;
}}

.metric-label {{
    font-size: 14px;
    color: #B8C7DA;
    font-weight: 800;
    letter-spacing: 1px;
}}

.metric-value {{
    font-size: 29px;
    font-weight: 800;
    color: white;
    margin-top: 8px;
}}

.metric-note {{
    font-size: 14px;
    color: #B8C7DA;
    margin-top: 5px;
}}

.panel {{
    background: linear-gradient(145deg,#121F32,#0D1726);
    border: 1px solid #223650;
    border-radius: 18px;
    padding: 18px;
}}

.panel-head {{
    font-size: 18px;
    font-weight: 700;
    color: #EDF3FC;
    margin-bottom: 5px;
}}

.panel-sub {{
    font-size: 14px;
    color: #AAB8CC;
    margin-bottom: 14px;
}}

.telemetry {{
    background: #101D30;
    border: 1px solid #233852;
    border-radius: 13px;
    padding: 15px;
}}

.t-label {{
    font-size: 14px;
    color: #B8C7DA;
    font-weight: 800;
}}

.t-value {{
    font-size: 22px;
    font-weight: 700;
    color: white;
    margin-top: 7px;
}}

.t-unit {{
    font-size: 13px;
    color: #AAB8CC;
}}

.status {{
    display: inline-block;
    padding: 8px 12px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 800;
}}

.status-blue {{
    color: #9CC8FF;
    background: rgba(67,139,255,.10);
    border: 1px solid rgba(67,139,255,.3);
}}

.status-red {{
    color: #FF9AA5;
    background: rgba(255,83,100,.10);
    border: 1px solid rgba(255,83,100,.3);
}}

.insight {{
    background: linear-gradient(100deg,rgba(67,139,255,.15),rgba(72,221,242,.06));
    border-left: 4px solid {BLUE};
    border-radius: 9px;
    padding: 15px;
    color: #D5E2F2;
    font-size: 15px;
    line-height: 1.7;
}}

.stButton button {{
    background: linear-gradient(100deg,#2563C9,#167B9B);
    color: white;
    border: 1px solid {BLUE};
    border-radius: 10px;
    font-weight: 700;
}}

[data-testid="stProgressBar"] > div > div {{
    background: linear-gradient(90deg,{BLUE},{CYAN}) !important;
}}

[data-testid="stAlert"] {{
    background: #14243A !important;
    border: 1px solid #2A4261;
    color: white !important;
}}

[data-testid="stPlotlyChart"] {{
    border: 1px solid #223650;
    border-radius: 16px;
    background: rgba(15,26,43,.55);
    padding: 5px;
}}

.footer {{
    border-top: 1px solid #263B57;
    padding-top: 16px;
    margin-top: 28px;
    color: #AAB8CC;
    font-size: 14px;
}}

@media (max-width: 900px) {{
    .block-container {{
        padding: 1rem;
    }}
    .hero {{
        padding: 20px;
    }}
}}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown(
        "<div style='font-size:28px;font-weight:800;color:white'>⚡ VoltIQ</div>"
        "<div style='font-size:12px;letter-spacing:2px;color:#AAB8CC'>EV INTELLIGENCE SYSTEM</div>",
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("<div class='kicker'>WORKSPACE</div>", unsafe_allow_html=True)

    page = st.radio(
        "PAGES",
        [
            "Command Center",
            "Charging Studio",
            "Trip Planner",
            "Energy Analytics",
            "Battery Condition"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("<div class='kicker'>VEHICLE CONFIGURATION</div>", unsafe_allow_html=True)

    capacity = st.number_input(
        "Battery capacity · kWh",
        10.0, 200.0, 60.0, 1.0
    )

    soc = st.slider("Current charge · %", 0, 100, 80)

    consumption = st.number_input(
        "Energy consumption · kWh/km",
        0.05, 1.00, 0.18, 0.01,
        format="%.2f"
    )

    power = st.slider("Charger power · kW", 1, 50, 7)

    st.caption("Change these inputs to explore different operating scenarios.")

    st.divider()

    st.markdown(
        "<div class='kicker'>SYSTEM</div>"
        "<span class='status status-blue'>● SIMULATION MODE</span>",
        unsafe_allow_html=True
    )


# ---------------- CALCULATIONS ----------------
energy = capacity * soc / 100

range_km = energy / consumption if consumption > 0 else 0

charge_hours = max(0, (capacity - energy) / power)

low = soc <= 25


# ---------------- REUSABLE FUNCTIONS ----------------
def metric_card(label, value, note, icon):

    st.markdown(
        f"""
        <div class='metric-card'>
            <div class='metric-label'>{label} {icon}</div>
            <div class='metric-value'>{value}</div>
            <div class='metric-note'>{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def telemetry_card(label, value, unit, icon):

    st.markdown(
        f"""
        <div class='telemetry'>
            <div class='t-label'>{icon} &nbsp; {label}</div>
            <div class='t-value'>{value} <span class='t-unit'>{unit}</span></div>
        </div>
        """,
        unsafe_allow_html=True
    )


def chart_layout(fig, height=310):

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(8,16,28,.55)",
        font={"color": MUTED, "family": "DM Sans"},
        height=height,
        margin=dict(l=12, r=15, t=25, b=20),
        hoverlabel=dict(bgcolor="#14243A", font_color=WHITE),
        xaxis=dict(gridcolor="#20324A", zerolinecolor="#20324A"),
        yaxis=dict(gridcolor="#20324A", zerolinecolor="#20324A")
    )

    return fig


# ==================================================
# COMMAND CENTER
# ==================================================
if page == "Command Center":

    left, right = st.columns([1.35, 1], gap="large")

    with left:

        st.markdown(
            f"""<div class="hero">
<div class="eyebrow">VOLTIQ / COMMAND CENTER</div>

<div class="hero-title">
Electric mobility.<br>
<span style="color:{CYAN}">Made intelligent.</span>
</div>

<div class="hero-copy">
A focused view of your vehicle's energy, range and battery condition.
Explore operating scenarios with clear estimates.
</div>

<div class="hero-stat">
<div><b>{soc}%</b><span>STATE OF CHARGE</span></div>
<div><b>{range_km:.0f} km</b><span>ESTIMATED RANGE</span></div>
<div><b>{capacity:.0f} kWh</b><span>PACK CAPACITY</span></div>
</div>
</div>""",
            unsafe_allow_html=True
        )

    with right:

        car_candidates = [
            os.path.join("assets", "tesla_side.png"),
            os.path.join("assets", "ev_car.jpg")
        ]

        car_path = next(
            (path for path in car_candidates if os.path.exists(path)),
            None
        )

        if car_path:

            st.image(car_path, use_container_width=True)

            st.markdown(
                "<div style='text-align:center;margin-top:8px;"
                "font-size:17px;font-weight:800;letter-spacing:1.5px;"
                "color:#D5E2F2'>CAR IMAGE</div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                "<div class='panel' style='text-align:center;padding:60px'>"
                "<div style='font-size:65px'>🚘</div>"
                "<div class='panel-head'>Electric Vehicle</div>"
                "</div>",
                unsafe_allow_html=True
            )

            st.caption("Add tesla_side.png or ev_car.jpg inside the assets folder.")

    st.write("")

    st.markdown("<div class='kicker'>AT A GLANCE</div>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("AVAILABLE ENERGY", f"{energy:.1f} kWh", "Estimated energy in pack", "⚡")

    with c2:
        metric_card("DRIVING RANGE", f"{range_km:.0f} km", "Based on entered consumption", "↗")

    with c3:
        metric_card("CHARGE TO FULL", f"{charge_hours:.1f} h", "Constant-power estimate", "⌁")

    with c4:
        metric_card("BATTERY CONDITION", "95%*", "Illustrative health value", "◇")

    st.write("")

    a, b = st.columns([1, 1.45], gap="large")

    with a:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Energy reserve</div>"
            "<div class='panel-sub'>Current state of charge</div>",
            unsafe_allow_html=True
        )

        color = RED if low else BLUE

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=soc,
                number={"suffix": "%", "font": {"size": 39, "color": WHITE}},
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": MUTED
                    },
                    "bar": {"color": color, "thickness": .24},
                    "bgcolor": "#1B2A40",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 25], "color": "#3A202B"},
                        {"range": [25, 100], "color": "#1A3556"}
                    ]
                }
            )
        )

        gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color=WHITE,
            height=240,
            margin=dict(l=15, r=15, t=12, b=0)
        )

        st.plotly_chart(gauge, use_container_width=True)

        st.progress(soc / 100)

        if low:
            st.markdown(
                "<span class='status status-red'>● LOW CHARGE · PLAN A STOP</span></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<span class='status status-blue'>● ENERGY RESERVE NORMAL</span></div>",
                unsafe_allow_html=True
            )

    with b:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Projected discharge</div>"
            "<div class='panel-sub'>Illustrative battery trend · fixed hourly decrease</div>",
            unsafe_allow_html=True
        )

        hours = list(range(7))
        levels = [max(0, soc - i * 8) for i in hours]

        fig = go.Figure()

        for i in range(len(hours) - 1):

            col = RED if levels[i] <= 25 or levels[i + 1] <= 25 else BLUE

            fig.add_trace(
                go.Scatter(
                    x=hours[i:i+2],
                    y=levels[i:i+2],
                    mode="lines",
                    line={"color": col, "width": 3},
                    showlegend=False
                )
            )

        fig.add_trace(
            go.Scatter(
                x=hours,
                y=levels,
                mode="markers",
                marker={"color": "white", "size": 8},
                showlegend=False
            )
        )

        fig.add_hline(
            y=25,
            line_dash="dot",
            line_color=RED
        )

        chart_layout(fig, 260)

        fig.update_layout(
            xaxis_title="Elapsed time (hours)",
            yaxis_title="Battery charge (%)",
            yaxis_range=[0, 100]
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown(
            f"""
            <div style='font-size:14px;color:{MUTED}'>
            <span style='color:{BLUE}'>●</span> Normal range &nbsp;
            <span style='color:{RED}'>●</span> Low-charge zone &nbsp;
            <span style='color:white'>●</span> Data point
            </div></div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.markdown(
        "<div class='kicker'>VEHICLE TELEMETRY · SCENARIO VIEW</div>",
        unsafe_allow_html=True
    )

    t1, t2, t3, t4 = st.columns(4)

    with t1:
        telemetry_card("PACK VOLTAGE", f"{300 + soc*1.2:.0f}", "V · illustrative", "⚡")

    with t2:
        telemetry_card(
            "PACK CURRENT",
            f"{(power*1000/max(1,300+soc*1.2)):.1f}",
            "A · charge scenario",
            "↯"
        )

    with t3:
        telemetry_card("BATTERY TEMP", "25", "°C · placeholder", "◉")

    with t4:
        telemetry_card("OPERATING MODE", "READY", "simulation state", "●")

    st.markdown(
        "<div class='insight'><b>Energy insight</b><br>" +
        (
            "Charge is at or below 25%. Consider planning a charging stop."
            if low else
            f"At the entered consumption of {consumption:.2f} kWh/km, "
            f"estimated range is about {range_km:.0f} km."
        ) +
        "</div>",
        unsafe_allow_html=True
    )

    st.caption(
        "Battery health, voltage, current and temperature are illustrative values, "
        "not readings from a connected vehicle."
    )


# ==================================================
# CHARGING STUDIO
# ==================================================
elif page == "Charging Studio":

    st.markdown("<div class='eyebrow'>ENERGY / REPLENISHMENT</div>", unsafe_allow_html=True)

    st.title("Charging Studio")

    st.markdown(
        "<div class='muted'>Understand your next charge before you plug in.</div>",
        unsafe_allow_html=True
    )

    left, right = st.columns(2, gap="large")

    with left:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Charging session</div>"
            "<div class='panel-sub'>Estimated session progress</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div style='font-size:48px;font-weight:800;color:{CYAN}'>{soc}%</div>",
            unsafe_allow_html=True
        )

        st.progress(soc / 100)

        x, y = st.columns(2)

        with x:
            st.metric("Energy to full", f"{capacity-energy:.1f} kWh")

        with y:
            st.metric("Estimated duration", f"{charge_hours:.2f} hrs")

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Charging profile</div>"
            "<div class='panel-sub'>Simplified constant-power assumption</div>",
            unsafe_allow_html=True
        )

        vals = [
            soc,
            min(100, soc + power * 0.8),
            min(100, soc + power * 1.6),
            min(100, soc + power * 2.4)
        ]

        f = go.Figure(
            go.Scatter(
                x=["Now", "+1 hr", "+2 hrs", "+3 hrs"],
                y=vals,
                mode="lines+markers",
                line={"color": CYAN, "width": 3},
                marker={"color": "white", "size": 8}
            )
        )

        chart_layout(f, 270)

        f.update_layout(
            yaxis_title="Estimated charge (%)",
            yaxis_range=[0, 100]
        )

        st.plotly_chart(f, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='insight'>Charging time is calculated as remaining energy "
        "divided by charger power. Real EV charging varies with temperature, "
        "charger limits and battery management.</div>",
        unsafe_allow_html=True
    )


# ==================================================
# TRIP PLANNER
# ==================================================
elif page == "Trip Planner":

    st.markdown("<div class='eyebrow'>JOURNEY / ENERGY PLANNING</div>", unsafe_allow_html=True)

    st.title("Trip Planner")

    st.markdown(
        "<div class='muted'>Check whether your current energy estimate covers the journey.</div>",
        unsafe_allow_html=True
    )

    trip = st.number_input(
        "Planned trip distance · km",
        min_value=0.0,
        max_value=2000.0,
        value=100.0,
        step=5.0
    )

    reserve = st.slider("Desired arrival reserve · %", 0, 50, 10)

    used = trip * consumption
    remaining = energy - used

    remaining_pct = remaining / capacity * 100 if capacity else 0

    a, b, c = st.columns(3)

    with a:
        metric_card("TRIP ENERGY", f"{used:.1f} kWh", "Estimated energy required", "↗")

    with b:
        metric_card(
            "ARRIVAL CHARGE",
            f"{max(0, remaining_pct):.1f}%",
            "Estimated charge on arrival",
            "⌁"
        )

    with c:
        metric_card("ENERGY BUFFER", f"{remaining:.1f} kWh", "After planned trip", "⚡")

    if remaining < 0:

        st.error(
            f"Energy estimate is short by {abs(remaining):.1f} kWh. "
            "A charging stop is needed."
        )

    elif remaining_pct < reserve:

        st.warning(
            f"Arrival charge ({remaining_pct:.1f}%) is below your "
            f"selected {reserve}% reserve."
        )

    else:

        st.success(
            f"The trip fits within the estimate, with about "
            f"{remaining_pct:.1f}% charge remaining."
        )

    st.markdown(
        "<div class='panel'><div class='panel-head'>Journey energy breakdown</div>"
        "<div class='panel-sub'>Energy remaining after the planned trip</div>",
        unsafe_allow_html=True
    )

    f = go.Figure(
        go.Scatter(
            x=["Trip start", "After trip"],
            y=[energy, max(0, remaining)],
            mode="lines+markers+text",
            line={"color": BLUE, "width": 3},
            marker={"color": "white", "size": 9},
            text=[f"{energy:.1f} kWh", f"{max(0,remaining):.1f} kWh"],
            textposition="top center"
        )
    )

    chart_layout(f, 280)

    f.update_layout(yaxis_title="Remaining energy (kWh)")

    st.plotly_chart(f, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# ENERGY ANALYTICS
# ==================================================
elif page == "Energy Analytics":

    st.markdown("<div class='eyebrow'>DATA / PERFORMANCE</div>", unsafe_allow_html=True)

    st.title("Energy Analytics")

    st.markdown(
        "<div class='muted'>Explore how battery charge and consumption shape your estimated range.</div>",
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        metric_card("AVAILABLE ENERGY", f"{energy:.1f} kWh", "Current input scenario", "⚡")

    with b:
        metric_card("ESTIMATED RANGE", f"{range_km:.1f} km", "At entered efficiency", "↗")

    with c:
        metric_card("CONSUMPTION", f"{consumption:.2f}", "kWh per km", "⌁")

    left, right = st.columns([1.35, 1], gap="large")

    with left:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Charge trend scenario</div>"
            "<div class='panel-sub'>Illustrative fixed-rate discharge, not measured history</div>",
            unsafe_allow_html=True
        )

        h = list(range(9))
        vals = [max(0, soc - i * 6) for i in h]

        f = go.Figure(
            go.Scatter(
                x=h,
                y=vals,
                mode="lines+markers",
                line={"color": BLUE, "width": 3},
                marker={"color": "white", "size": 8}
            )
        )

        f.add_hline(y=25, line_dash="dot", line_color=RED)

        chart_layout(f, 330)

        f.update_layout(
            xaxis_title="Elapsed hours",
            yaxis_title="Charge (%)",
            yaxis_range=[0, 100]
        )

        st.plotly_chart(f, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Consumption scenarios</div>"
            "<div class='panel-sub'>Estimated range at different efficiency levels</div>",
            unsafe_allow_html=True
        )

        eff = [0.14, 0.16, 0.18, 0.20, 0.22, 0.25]

        ranges = [energy / e for e in eff]

        f2 = go.Figure(
            go.Scatter(
                x=eff,
                y=ranges,
                mode="lines+markers",
                line={"color": CYAN, "width": 3},
                marker={"color": "white", "size": 8}
            )
        )

        chart_layout(f2, 330)

        f2.update_layout(
            xaxis_title="Consumption (kWh/km)",
            yaxis_title="Estimated range (km)"
        )

        st.plotly_chart(f2, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='insight'>Lower energy consumption increases the estimated "
        "distance available from the same battery charge. Real-world range also "
        "depends on speed, weather, terrain, payload and driving style.</div>",
        unsafe_allow_html=True
    )


# ==================================================
# BATTERY CONDITION
# ==================================================
elif page == "Battery Condition":

    st.markdown("<div class='eyebrow'>BATTERY / CONDITION</div>", unsafe_allow_html=True)

    st.title("Battery Condition")

    st.markdown(
        "<div class='muted'>Explore the effect of an estimated state-of-health value on usable capacity.</div>",
        unsafe_allow_html=True
    )

    health = st.slider("Estimated state of health · %", 50, 100, 95)

    usable = capacity * health / 100

    a, b, c = st.columns(3)

    with a:
        metric_card("STATE OF HEALTH", f"{health}%", "User-entered estimate", "◇")

    with b:
        metric_card("USABLE CAPACITY", f"{usable:.1f} kWh", "Capacity × health estimate", "⚡")

    with c:
        metric_card("CAPACITY DIFFERENCE", f"{capacity-usable:.1f} kWh", "Compared with nominal", "↘")

    left, right = st.columns([1, 1], gap="large")

    with left:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Capacity condition</div>"
            "<div class='panel-sub'>Estimated usable capacity vs nominal capacity</div>",
            unsafe_allow_html=True
        )

        f = go.Figure(
            go.Scatter(
                x=["Nominal capacity", "Usable estimate"],
                y=[capacity, usable],
                mode="lines+markers+text",
                line={"color": BLUE, "width": 3},
                marker={"color": "white", "size": 9},
                text=[f"{capacity:.1f} kWh", f"{usable:.1f} kWh"],
                textposition="top center"
            )
        )

        chart_layout(f, 280)

        f.update_layout(yaxis_title="Capacity (kWh)")

        st.plotly_chart(f, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown(
            "<div class='panel'><div class='panel-head'>Condition note</div>"
            "<div class='panel-sub'>Interpretation of the value you entered</div>",
            unsafe_allow_html=True
        )

        if health >= 90:

            st.markdown(
                "<span class='status status-blue'>STRONG ESTIMATE</span>",
                unsafe_allow_html=True
            )

            note = "The entered estimate indicates relatively high remaining capacity."

        elif health >= 75:

            st.markdown(
                "<span class='status status-blue'>MODERATE ESTIMATE</span>",
                unsafe_allow_html=True
            )

            note = "The entered estimate indicates some reduction in available capacity."

        else:

            st.markdown(
                "<span class='status status-red'>LOWER CAPACITY ESTIMATE</span>",
                unsafe_allow_html=True
            )

            note = "The entered estimate indicates a more noticeable reduction in available capacity."

        st.write("")

        st.markdown(
            f"""
            <div style='font-size:42px;font-weight:800;color:{CYAN}'>
                {health}%
            </div>
            <div style='color:{MUTED};font-size:14px'>
                ESTIMATED STATE OF HEALTH
            </div>
            <p style='margin-top:18px;color:#C3D0E1;font-size:15px'>
                {note}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    st.warning(
        "This is a user-entered estimate, not a battery diagnostic. "
        "Actual state of health requires validated measurements and vehicle-specific data."
    )


# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class='footer'>
        VOLTIQ · EV INTELLIGENCE &nbsp; / &nbsp;
        DEMONSTRATION BUILD &nbsp; · &nbsp;
        Scenario estimates only — not connected vehicle telemetry.
    </div>
    """,
    unsafe_allow_html=True
)