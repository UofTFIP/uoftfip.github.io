python update_abstracts.py
python print_abstracts.py

cd _abstracts/

# change markdown for pandoc
sed -i 's/<sup>/^/g' all_abstracts.md
sed -i 's_</sup>_^_g' all_abstracts.md
sed -i 's/__/_/g' all_abstracts.md

sed -i 's/<sup>/^/g' orals_only.md
sed -i 's_</sup>_^_g' orals_only.md
sed -i 's/__/_/g' orals_only.md

# use reference doc for formatting
pandoc all_abstracts.md -o abstracts.docx --reference-doc reference.docx
pandoc orals_only.md -o orals.docx --reference-doc reference.docx
