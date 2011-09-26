from distutils.core import setup

setup(name ="html-hyphenator",
      version ="1.0",
      description = "CLI tool for hyphenating the HTML files",
      author = "Vasudev Kamath",
      author_email = "kamathvasudev@gmail.com",
      url = "",
      py_modules = ['libhtmlhyphenate'],
      scripts = ["html-hyphenator"],
      requires = ["hypy"],
      data_files = [("share/man/man1",["html-hyphenator.1"])
                    ])
