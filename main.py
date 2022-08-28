import re

def func1(query):
    res = re.findall(r'\(.*?\)', query)
    word = "FROM"
    for t in res:
        if word in t:
            x = re.split('FROM | WHERE ', t)
            tbl = x[1]
            # print (t)
            t1 = "{}".format(t)
            query = query.replace(t1, tbl)

    return query
def func2(query1):
    # Use a breakpoint in the code line below to debug your script.
    query = func1(query1)
    query = re.sub(r"[\n\t\(\)]*", "", query)
    result = re.split('SELECT |FROM | WHERE ', query)
    lst1 = []
    lst2 = []
    tpl = ()
    for s in result[2].split(", "):
        # print(s)
        for T in reversed(s.split(" ")):
            T = T.strip()
            lst1.append(T)
            tpl = lst1
        lst1 = []
        lst2.append(tpl)
    #print(lst2)
    d1 = dict(lst2)
    lst1 = []
    lst2 = []
    tpl = ()
    # print(result[1])
    r2 = re.split(",", result[1])
    # print(r2)
    for s in r2:
        # print(s)
        r2 = re.split("\.", s)
        for T in reversed(r2):
            T = T.strip()
            lst1.append(T)
            tpl = lst1
        lst1 = []
        lst2.append(tpl)
    # print(lst2)
    # print (result[0],result[1],result[2])
    d2 = dict(lst2)
    # print(d1)
    # print(d2)
    for p in d2.keys():
        col1 = d2[p]
        tbl = d1[col1]
        print(" column value is {} and table is {}".format(p, tbl))
        # print(col1)
        # print(d2[col1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    query = "LOCKING ROW FOR ACCESS SELECT T.SWB_CNTRY_ID, T.CNTRY_TYPE_CD, T.DW_EFF_DT, S.DW_AS_OF_DT FROM (SELECT SWB_CNTRY_ID, CNTRY_TYPE_CD, RCV_IN, DW_EFF_DT, MAXDW_EFF_DT MAX_EFF_DT FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T WHERE CURR_IN=1 GROUP BYa 1,2,3,4) T, (SELECT SWB_CNTRY_ID, CNTRY_SCHEME_CD, DW_AS_OF_DT, DW_ACTN_IND FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S WHERE S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD AND (S.DW_SCTN_IND=U OR (S.DW_ACTN_IND=I AND T.RCV_IN=0)) AND S.DW_AS_OF_DT > T.MAX_EFF_DT "

    func2(query)


