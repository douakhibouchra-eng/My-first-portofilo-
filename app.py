import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="معرض أعمالي | مساعد الصيدلي الذكي",
    page_icon="💻",
    layout="centered"
)

# تطبيق الألوان والتنسيقات الفاخرة للغة العربية والألوان الصيدلانية
st.markdown("""
    <style>
    /* ضبط اتجاه النصوص والقوائم للغة العربية */
    .stMarkdown, .stSelectbox, .stAlert, div.stTabs {
        direction: rtl;
        text-align: right;
    }
    h1, h2, h3 {
        color: #1e7e34 !important;
        text-align: right;
    }
    /* تخصيص مظهر الأزرار */
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #218838;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 2. إنشاء الأقسام (Tabs) أعلى الصفحة لجمع العملين معاً
tab1, tab2 = st.tabs(["👤 الهوية الرقمية والتعريف", "💊 أداة مساعد الصيدلي الذكي"])

# ==========================================
# القسم الأول: معرض الأعمال والتعريف الشخصي
# ==========================================
with tab1:
    st.title("👋 أهلاً بك في موقعي الشخصي")
    st.subheader("أنا مبرمجة شغوفة برؤية المستقبل وتطوير الحلول البرمجية")
    st.write("أستخدم لغة Python لبناء أدوات برمجية ذكية ومواقع تفاعلية مبتكرة تجمع بين العلم والتكنولوجيا.")
    
    st.markdown("---")
    st.header("🛠️ مهاراتي التقنية")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("🐍 البرمجة بلغة Python")
        st.info("📊 بناء الأنظمة الخبيرة وتحليل البيانات")
    with col2:
        st.info("💻 تطوير واجهات المستخدم بـ Streamlit")
        st.success("⚙️ إدارة المشاريع البرمجية عبر GitHub")
        
    st.markdown("---")
    st.header("📞 تواصل معي")
    st.write("يسعدني دائماً تواصلك معي للنقاش حول المشاريع أو الفرص المتاحة:")
    st.link_button("🌐 تصفح حسابي على GitHub", "https://github.com")
    st.link_button("📧 أرسل لي بريداً إلكترونياً", "mailto:your-email@example.com")

# ==========================================
# القسم الثاني: مشروع مساعد الصيدلي الذكي
# ==========================================
with tab2:
    # قاعدة بيانات التداخلات الدوائية
    INTERACTIONS_DB = {
        "إيبوبروفين (Ibuprofen)": {
            "الأسبرين (Aspirin)": {"level": "high", "note": "يزيد من خطر حدوث نزيف في المعدة ويقلل من فاعلية الأسبرين لحماية القلب."},
            "مضادات تخثر الدم (Warfarin)": {"level": "high", "note": "تداخل خطير جداً؛ يزيد من احتمالية حدوث نزيف حاد."},
            "مكملات البوتاسيوم": {"level": "medium", "note": "قد يؤدي الجمع بينهما إلى زيادة مستويات البوتاسيوم في الدم بشكل يضر بالكلى."}
        },
        "الباراسيتامول (Paracetamol)": {
            "مضادات تخثر الدم (Warfarin)": {"level": "medium", "note": "الاستخدام المنتظم بجرعات عالية من الباراسيتامول قد يزيد من تأثير الوارفارين وخطر النزيف."},
            "أدوية الصرع (Phenytoin)": {"level": "medium", "note": "قد يقلل من فاعلية الباراسيتامول ويزيد من إجهاد الكبد."}
        },
        "سيبروفلوكساسين (Ciprofloxacin - مضاد حيوي)": {
            "مكملات الحديد أو الكالسيوم": {"level": "high", "note": "المعادن ترتبط بالمضاد الحيوي وتمنع امتصاصه في الجسم تماماً، مما يفقد الدواء مفعوله."},
            "البروفين": {"level": "medium", "note": "قد يزيد من خطر حدوث تشنجات في حالات نادرة."}
        }
    }

    st.title("💊 نظام مساعد الصيدلي الذكي")
    st.write("نظام خبير فوري لفحص التداخلات الدوائية لحماية المرضى وتقليل الأخطاء البشرية.")
    
    st.write("### 🔍 فحص التداخل الدوائي")
    
    medications = list(INTERACTIONS_DB.keys())
    all_meds = set(medications)
    for med in INTERACTIONS_DB:
        all_meds.update(INTERACTIONS_DB[med].keys())
    all_meds_list = sorted(list(all_meds))
    
    c1, c2 = st.columns(2)
    with c1:
        med1 = st.selectbox("اختر الدواء الأول (الرئيسي):", ["-- اختر الدواء --"] + medications, key="med1")
    with c2:
        med2 = st.selectbox("اختر الدواء الثاني (المكمل):", ["-- اختر الدواء --"] + all_meds_list, key="med2")
        
    if st.button("افحص التداخل الآن"):
        if med1 == "-- اختر الدواء --" or med2 == "-- اختر الدواء --":
            st.warning("⚠️ يرجى اختيار دواءين صالحين لبدء الفحص.")
        elif med1 == med2:
            st.info("💡 لقد قمتِ باختيار نفس الدواء، لا يوجد تداخل دوائي.")
        else:
            has_interaction = False
            detail = None
            
            if med1 in INTERACTIONS_DB and med2 in INTERACTIONS_DB[med1]:
                detail = INTERACTIONS_DB[med1][med2]
                has_interaction = True
            elif med2 in INTERACTIONS_DB and med1 in INTERACTIONS_DB[med2]:
                detail = INTERACTIONS_DB[med2][med1]
                has_interaction = True
                
            if has_interaction:
                if detail["level"] == "high":
                    st.error("🚨 **تداخل عالي الخطورة (خطر)!**")
                    st.markdown(f"**التفاصيل الطبية:** {detail['note']}")
                elif detail["level"] == "medium":
                    st.warning("⚠️ **تداخل متوسط الخطورة (انتباه):**")
                    st.markdown(f"**التفاصيل الطبية:** {detail['note']}")
            else:
                st.success("✅ **آمن:** لا يوجد تداخل دوائي معروف بين هذين الدواءين في قاعدة البيانات الحالية.")

    st.markdown("---")
    st.write("### 🛠️ نظرة برمجية خلف الكواليس")
    st.info("""
    يعتمد هذا النظام على خوارزميات البحث في الهياكل البيانية المتداخلة (Nested Dictionaries) لتقديم استجابة فورية فائقة السرعة، 
    مما يوضح مهارات مطور البرمجيات في تحويل المعرفة العلمية المتخصصة إلى حلول تقنية ذكية وعملية.
    """)

st.markdown("---")
st.caption("تم تطوير هذا الموقع المدمج بكل شغف 💻")
