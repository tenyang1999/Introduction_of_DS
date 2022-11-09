# problem2
# input and preprocess data
with open('IMDB-Movie-Data.csv','r') as f:
    title = f.readline().rstrip() #刪除尾隨字元
    title = title.split(",") #以,分割

    data_dict = {i:[] for i in title}
    value_list = list(data_dict.values())
    
    for line in f.readlines():
        line = line.split(",")
        for i in range(len(value_list)):
            if "\n" in line[i]:
                value = line[i].rstrip()
                if value == "":
                    value = "0"
                value_list[i].append(value)
            else:
                if line[i] == "":
                    line[i] = "0"
                    value_list[i].append(line[i])
                else:
                    value_list[i].append(line[i])

# Q2.1(done)(rating has been sorted)
rating_2016 = []
index_2016 = []
for i in range(len(data_dict["Year"])):
    if data_dict["Year"][i] == "2016":
        rating_2016.append(data_dict["Rating"][i])
        if len(rating_2016) <= 3:
        #sort rating
            print(data_dict["Title"][i])
# Ans:Dangal,Kimi No na wa,Koe no katachi

# Q2.2(done)
actor_list = []
earn_list = []
for i in range(len(data_dict["Actors"])):
    actors = data_dict["Actors"][i].split("|")
    for j in actors:
        if j not in actor_list:
            actor_list.append(j)

for i in range(len(actor_list)):
    earn = []
    for j in range(len(data_dict["Actors"])):
        if actor_list[i] in data_dict["Actors"][j]:
            if data_dict["Revenue (Millions)"][j] == "0":
                pass
            else:
                earn.append(float(data_dict["Revenue (Millions)"][j]))
    if earn == []:
        earn_list.append(0)
    else:
        earn = sum(earn)/len(earn)
        earn_list.append(earn)

top1 = earn_list[0]
for i in range(len(earn_list)):
    if earn_list[i] > top1:
        max_ind = i
print(actor_list[max_ind])

# Q2.3(done)
rating_emma = []
for i in range(len(data_dict["Actors"])):
    if "Emma Watson" in data_dict["Actors"][i]:
        rating_emma.append(float(data_dict["Rating"][i]))
print(sum(rating_emma)/len(rating_emma))
# Ans:7.175

# Q2.4(done)
director_list = []
cowork_list = []
for i in range(len(data_dict["Director"])):
    if data_dict["Director"][i] not in director_list:
        director_list.append(data_dict["Director"][i])
    # actors = data_dict["Actors"][i].split("|")
    # cowork = []
    # for j in actors:
    #     if j not in cowork:
    #         cowork.append(j)
    # cowork_list.append(cowork)
for i in range(len(director_list)):
    cowork = []
    for j in range(len(data_dict["Actors"])):
        actors = data_dict["Actors"][j].split("|")
        if director_list[i] == data_dict["Director"][j]:
            for k in actors:
                if k not in cowork:
                    cowork.append(k)
    cowork_list.append(len(cowork))
print(sorted(list(zip(director_list,cowork_list)),key=lambda x:x[1],reverse=True)[:3])

# Q2.5(done)
actor_list = []
genre_list = []
for i in range(len(data_dict["Actors"])):
    actors = data_dict["Actors"][i].split("|")
    for j in actors:
        if j not in actor_list:
            actor_list.append(j)
for i in range(len(actor_list)):
    genre = []
    for j in range(len(data_dict["Genre"])):
        genres = data_dict["Genre"][j].split("|")
        if actor_list[i] in data_dict["Actors"][j]:
            for k in genres:
                if k not in genre:
                    genre.append(k)
    genre_list.append(len(genre))
sort_genre_list = sorted(list(zip(actor_list,genre_list)),key=lambda x:x[1],reverse=True)
top2 = []
for i in range(len(sort_genre_list)):
    if sort_genre_list[i][1] not in top2:
        top2.append(sort_genre_list[i][1])
    if len(top2) > 2:
        break
    if sort_genre_list[i][1] in top2:
        print(sort_genre_list[i])

# Q2.6(done)(8,9,10)
actor_list = []
year_list = []
for i in range(len(data_dict["Actors"])):
    actors = data_dict["Actors"][i].split("|")
    for j in actors:
        if j not in actor_list:
            actor_list.append(j)
for i in range(len(actor_list)):
    gap = 0
    years = []
    for j in range(len(data_dict["Title"])):
        if actor_list[i] in data_dict["Actors"][j]:
            years.append(int(data_dict["Year"][j]))
    gap = max(years)-min(years)
    year_list.append(gap)
sort_year_list = sorted(list(zip(actor_list,year_list)),key=lambda x:x[1],reverse=True)
top3 = []
for i in range(len(sort_year_list)):
    if sort_year_list[i][1] not in top3:
        top3.append(sort_year_list[i][1])
    if len(top3) > 3 :
        break
    if sort_year_list[i][1] in top3:
        print(sort_year_list[i])

# Q2.7(done)(Name space?)
co_john = []
for i in range(len(data_dict["Actors"])): #find directly collaborate
    actors = data_dict["Actors"][i].split("|")
    if "Johnny Depp" in actors:
        for j in range(len(actors)):
            if actors[j] == "Johnny Depp":
                pass
            else:
                if actors[j] not in co_john:
                    co_john.append(actors[j])
in_co_john = []
for i in range(len(co_john)):
    for j in range(len(data_dict["Actors"])):
        actors = data_dict["Actors"][j].split("|")
        if co_john[i] in actors:
            for k in range(len(actors)):
                if co_john[i] == actors[k]:
                    pass
                else:
                    if actors[k] not in co_john:
                        if actors[k] not in in_co_john:
                            if actors[k] != "Johnny Depp" and actors[k] != " Johnny Depp":
                               in_co_john.append(actors[k])
print(co_john)
print(in_co_john)