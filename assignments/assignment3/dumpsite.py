'''
cities = cities.filter(['Metropolitan area'])
    df5 = pd.merge(cities, df1, how='outer').rename(columns={'W-L%': 'NFL'})
    df5 = pd.merge(df5, df2, how='outer').rename(columns={'W/L%': 'NBA'})
    df5 = pd.merge(df5, df3, how='outer').rename(columns={'W-L%': 'MLB'})
    df5 = pd.merge(df5, df4, how='outer').rename(columns={'W/L%': 'NHL'})
    df5 = df5.filter(['NFL', 'NBA', 'NHL', 'MLB'])
    import scipy.stats as stats
   
    
    #    raise NotImplementedError()
    
    # Note: p_values is a full dataframe, so df.loc["NFL","NBA"] should be the same as df.loc["NBA","NFL"] and
    # df.loc["NFL","NFL"] should return np.nan
    #sports = ['NFL', 'NBA', 'NHL', 'MLB']
    #p_values = pd.DataFrame({k:np.nan for k in sports}, index=sports)

    group1 = df5.where(df5== df5['NBA']).dropna()['NBA']
    group2 = df5.where(df5==df5['NHL']).dropna()['NHL']


    print(group1)

    #assert abs(p_values.loc["NBA", "NHL"] - 0.02) <= 1e-2, "The NBA-NHL p-value should be around 0.02"
    #assert abs(p_values.loc["MLB", "NFL"] - 0.80) <= 1e-2, "The MLB-NFL p-value should be around 0.80"
  

'''
print(True == True)