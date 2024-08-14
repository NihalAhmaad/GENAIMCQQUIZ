from setuptools import setup, find_packages

setup(
    name='MCQGENERATOR',
    version='1.00',
    author='Nihal',
    install_requires=["groq","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)