judges = """Dr. Adria Giacca
Dr. Alexander Velumian
Dr. Andrea Jurisicova
Dr. Ashley Untereiner
Dr. Azadeh Yeganeh
Dr. Battsetseg Batchuluun
Dr. Behzad Yeganeh
Dr. Boriss Sagalajev
Dr. Brubaker
Dr. Denise Belsham
Dr. Dianshi Wang
Dr. Evelyn Lambe
Dr. Evelyn Lambe
Dr. Frances Skinner
Dr. Guinever Imperio
Dr. Haibo Zhang
Dr. Haneesha Mohan
Dr. Heyu Ni
Dr. Hiro Hamada
Dr. J Min
Dr. James Eubanks
Dr. Jason Arsenault
Dr. Jeff Kroetsch
Dr. Jon Rocheleau
Dr. Justin Kenney
Dr. Keith Dadson
Dr. Lubna Nadeem
Dr. Mei Zhen
Dr. Mekayla Storer
Dr. Michael Litvack
Dr. Mike Wheeler
Dr. Phyllis Billia
Dr. R Sambathkumar
Dr. Richard Horner
Dr. Saifur Khan
Dr. Samaneh Yazdanikivi
Dr. Saumel Ahmadi
Dr. Stephanie Ratte
Dr. Stephen Matthews
Dr. Steve Prescott
Dr. Syme
Dr. William D Hutchison
Dr. Xiao-Yan Wen
Dr. Yasaman Aghazadeh
Dr. Zheng-Ping Jia
Dr. Zhong-Ping Feng"""

tag = "Judges - Presentations"

data = ["""- name: "{}"
  type: "{}"
""".format(judge, tag) for judge in judges.split("\n")]

data


data = "\n".join(data)
with open("_data/members.yml", 'a') as text_file:
    text_file.write(data)
