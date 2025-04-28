from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="deepseek_vl2",
    version="1.2.2",
    description="DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    license='MIT',
)
