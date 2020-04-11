import setuptools

setuptools.setup(
	name="memberboat",
	version="0.0.0",
	package_data={},
	classifiers=[
		"Development Status :: 1 - Planning",
		"Environment :: Console",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Topic :: Software Development",
	],
	entry_points={
		'console_scripts': [
			'memberboat = memberboat.__main__:main'
		],
	},
	python_requires=">=3.6",
	install_requires=["argparse==1.4.0", "attrs==19.3.0", "requests==2.14.0", "PyGithub==1.47"],
)
