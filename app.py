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
