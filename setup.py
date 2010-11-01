from distutils.core import setup

setup (name="geotiq",
       version="1.0",
       description="GEOTiQ Library",
       author="Daniel MacDougall",
       author_email="dmacdougall@gmail.com",
       url="http://github.com/dmacdougall/geotiq",
       packages=["geotiq"],
       requires=["lxml"]
)
