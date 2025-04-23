source_files := $(wildcard diagrams/*.gv)
output_files_tmp := $(source_files:.gv=.png)
output_files := $(addprefix static/,$(output_files_tmp))

all: $(output_files)

%.png : %.gv
	dot -Tpng -ostatic/$@ $<
