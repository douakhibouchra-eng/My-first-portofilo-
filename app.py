import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="معرض أعمالي | Portfolio", page_icon="💻", layout="centered")

# 2. العنوان الرئيسي والتعريف الشخصي
st.title("👋 أهلاً بك في موقعي الشخصي")
st.subheader("أنا مبرمجة شغوفة برؤية المستقبل وتطوير الحلول البرمجية")
st.write("أستخدم لغة Python لبناء أدوات برمجية ذكية ومواقع تفاعلية بسيطة.")

st.markdown("---")

# 3. قسم المهارات (Skills)
st.header("🛠️ مهاراتي التقنية")

# تقسيم المهارات على شكل أعمدة أنيقة
col1, col2 = st.columns(2)

with col1:
    st.success("🐍 البرمجة بلغة Python")
    st.info("📈 تحليل البيانات الأساسية")

with col2:
    st.info("💻 تطوير واجهات المستخدم بـ Streamlit")
    st.success("⚙️ التعامل مع أدوات البرمجة وبيئات العمل")

st.markdown("---")

# 4. قسم المشاريع (حتى لو كانت بسيطة، سنظهرها بشكل احترافي)
st.header("🚀 مشاريعي الحالية")

with st.expander("📌 مشروع 1: موقع معرض الأعمال الشخصي (هذا الموقع!)"):
    st.write("موقع ويب تفاعلي تم بناؤه بالكامل باستخدام لغة Python ومكتبة Streamlit لعرض الهوية البرمجية.")
    st.code("Language: Python (Streamlit)")

with st.expander("📌 مشروع 2: أداة تحليل بيانات مصغرة (قيد التطوير)"):
    st.write("برنامج بايثون يقوم بقراءة البيانات وحساب الإحصائيات الأساسية وعرضها للمستخدم.")
    st.code("Language: Python")

st.markdown("---")

# 5. قسم التواصل (Contact Me)
st.header("📞 تواصل معي")
st.write("يسعدني دائماً تواصلك معي للنقاش حول المشاريع أو الفرص المتاحة:")

# أزرار تفاعلية وروابط لتسهيل التواصل
st.link_button("🌐 تصفح حسابي على GitHub", "https://github.com")
st.link_button("📧 أرسل لي بريداً إلكترونياً", "mailto:your-email@example.com")

st.markdown("---")
st.caption("تم تطوير هذا الموقع بكل شغف باستخدام 🐍 Python")
import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="مساعد الصيدلي الذكي",
    page_icon="💊",
    layout="centered"
)

# تطبيق الألوان (أبيض، أخضر، أحمر) عبر ميزة الـ CSS المدمجة لجعل الواجهة راقية واحترافية
st.markdown("""
    <style>
    /* تغيير لون العناوين الرئيسية إلى الأخضر الصيدلاني المريح */
    h1, h2, h3 {
        color: #1e7e34 !important;
        text-align: right;
    }
    /* ضبط اتجاه النصوص للغة العربية */
    .stMarkdown, .stSelectbox, .stAlert {
        direction: rtl;
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
""", unsafe_index=True)

# 2. قاعدة البيانات المصغرة للتداخلات الدوائية (تعمل بالـ Logic في بايثون)
# تحتوي على الأدوية، تداخلاتها، مستوى الخطورة، والنصيحة الطبية
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

# 3. واجهة المستخدم الرسومية
st.title("💊 نظام مساعد الصيدلي الذكي")
st.subheader("أداة برمجية فورية لفحص التداخلات الدوائية وحماية المرضى")
st.write("قومي باختيار الدواء الأول والدواء الثاني ليفحص النظام التداخل بينهما تلقائياً بناءً على القواعد الطبية المخزنة.")

st.markdown("---")

# تصميم خانات الاختيار
st.write("### 🔍 فحص التداخل الدوائي")

# تجهيز قائمة الأدوية المتاحة
medications = list(INTERACTIONS_DB.keys())
# إضافة الأدوية التي تظهر كأدوية ثانوية أيضاً لضمان الشمولية
all_meds = set(medications)
for med in INTERACTIONS_DB:
    all_meds.update(INTERACTIONS_DB[med].keys())
all_meds_list = sorted(list(all_meds))

col1, col2 = st.columns(2)

with col1:
    med1 = st.selectbox("اختر الدواء الأول (أو الرئيسي):", ["-- اختر الدواء --"] + medications)

with col2:
    med2 = st.selectbox("اختر الدواء الثاني (أو المكمل):", ["-- اختر الدواء --"] + all_meds_list)

# 4. معالجة البيانات وإظهار النتيجة بناءً على الألوان المحددة (أخضر وأحمر)
if st.button("افحص التداخل الآن"):
    if med1 == "-- اختر الدواء --" or med2 == "-- اختر الدواء --":
        st.warning("⚠️ يرجى اختيار دواءين صالحين لبدء الفحص.")
    elif med1 == med2:
        st.info("💡 لقد قمتِ باختيار نفس الدواء، لا يوجد تداخل دوائي.")
    else:
        # البحث في قاعدة البيانات عن التداخل في الاتجاهين
        has_interaction = False
        detail = None
        
        if med1 in INTERACTIONS_DB and med2 in INTERACTIONS_DB[med1]:
            detail = INTERACTIONS_DB[med1][med2]
            has_interaction = True
        elif med2 in INTERACTIONS_DB and med1 in INTERACTIONS_DB[med2]:
            detail = INTERACTIONS_DB[med2][med1]
            has_interaction = True
            
        if has_interaction:
            # إذا كان التداخل خطير جداً يظهر باللون الأحمر
            if detail["level"] == "high":
                st.error(f"🚨 **تداخل عالي الخطورة (خطر)!**")
                st.markdown(f"**التفاصيل الطبية:** {detail['note']}")
            # إذا كان متوسط الخطورة يظهر بلون تنبيهي
            elif detail["level"] == "medium":
                st.warning(f"⚠️ **تداخل متوسط الخطورة (انتباه):**")
                st.markdown(f"**التفاصيل الطبية:** {detail['note']}")
        else:
            # إذا لم يكن هناك تداخل يظهر باللون الأخضر الصيدلاني الجميل
            st.success("✅ **آمن:** لا يوجد تداخل دوائي معروف بين هذين الدواءين في قاعدة البيانات الحالية. يمكن صرفهما معاً بحذر.")

st.markdown("---")

# 5. تذييل الصفحة لإبراز دوركِ كمطورة
st.write("### 🛠️ معلومات عن النظام (لأصحاب العمل)")
st.info("""
**ملاحظة برمجية:** تم بناء هذا النظام الخبير بالكامل باستخدام لغة **Python** ومكتبة **Streamlit**. 
يعتمد التطبيق على خوارزميات البحث في الهياكل البيانية المتداخلة (Nested Dictionaries) لتقديم استجابة فورية فائقة السرعة، 
مما يوضح كيفية تحويل المعرفة الطبية المعتمدة إلى حلول برمجية ذكية تساهم في تقليل الأخطاء البشرية داخل الصيدليات.
""")

st.caption("تم التطوير بكل شغف بواسطة مبرمجة النظم الخبيرة 💻")


