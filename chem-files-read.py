import pandas

#reading the files in DataFrame(df)
df1 = pandas.read_csv("LORef.csv")
df2 = pandas.read_csv("Problems.csv")
df3 = pandas.read_csv("Skills.csv")
df4 = pandas.read_csv("LOs.csv")

#merging the df1 and df4
df6 = df1[["Learning Objective ID","LO"]].merge(df4[["Learning Objective ID","Skill1", "Skill2","Skill3","Skill4","Skill5","Skill6"]], on="Learning Objective ID", how="left")

#finding problems related to each skill from Skills.csv and Problems.csv
problem_skill_list = []
for x in df3.index:
    sample_list = []
    problems_list2 = []
    los_list2 = []
    los_ref_list = []
    for y in df2.index:
        if df3.loc[x,"Skill"] == df2.loc[y,"Skill1"] or df3.loc[x,"Skill"] == df2.loc[y,"Skill2"] or df3.loc[x,"Skill"] == df2.loc[y,"Skill3"] or df3.loc[x,"Skill"] == df2.loc[y,"Skill4"] or df3.loc[x,"Skill"] == df2.loc[y,"Skill5"] or df3.loc[x,"Skill"] == df2.loc[y,"Skill6"]:
            problems_list1 = [df2.loc[y,"Resource"], df2.loc[y,"Problem"]]
            problems_list2.append(problems_list1)
    for z in df6.index:
        if df3.loc[x,"Skill"] == df6.loc[z,"Skill1"] or df3.loc[x,"Skill"] == df6.loc[z,"Skill2"] or df3.loc[x,"Skill"] == df6.loc[z,"Skill3"] or df3.loc[x,"Skill"] == df6.loc[z,"Skill4"] or df3.loc[x,"Skill"] == df6.loc[z,"Skill5"] or df3.loc[x,"Skill"] == df6.loc[z,"Skill6"]:
            los_ref_list = [df6.loc[z,"Learning Objective ID"], df6.loc[z,"LO"]]
            los_list2.append(los_ref_list)
    sample_list = [df3.loc[x,"Skill"], df3.loc[x,"Title"], problems_list2, los_list2]
    problem_skill_list.insert(x, sample_list)

#storing lists in df and converting df to csv
df5 = pandas.DataFrame(problem_skill_list,columns = ['Skill','Title','Problems List','Learning Objectives List'])
df5.to_csv("Results2.csv", index = False)




           
            
                    
        
