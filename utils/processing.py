from datetime import date


def creating_features(df,label=None):
    """Create a data frame with data and a feature
    
    Args:
        df (pandas.DataFrame, numpy.ndarray, mapping, or sequence): dataset containing all the info
        label - Optional (str): feature in the df
        
    Returns:
        Pandas like dataframe
    """
        
    df = df.copy()
    df['diasemana'] = df['mes'].dt.dayofweek
    df['mês'] = df['mes'].dt.month
    df['diamês'] = df['mes'].dt.day
    
    X = df[['diasemana','mês','diamês']]
    
    if label:
        y = df[label]
        return X,y
    return X
    