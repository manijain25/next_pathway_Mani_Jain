import re


def func1(query):
    # Use a breakpoint in the code line below to debug your script.
    result = re.split('SELECT |FROM | WHERE ', query)
    lst1 = []
    lst2 = []
    tpl = ()
    for s in result[2].split(", "):
        # print(s)
        for T in reversed(s.split(" ")):
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
    query = "LOCKING ROW FOR ACCESS SELECT T.SWB_CNTRY_ID,T.CNTRY_TYPE_CD,T.DW_EFF_DT,S.DW_AS_OF_DT FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T T, IDW_STAGE.CNTRY_MULTI_DEF_CD_S S WHERE S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD "
    func1(query)


