def hitta_största(tal_lista):
    
    """
    hittar största talet i listan
    
    kollar igenom lista och returna största talet
    
    argument:
    tal_lista(lista): lista med nummer
    
    returvärde: 
    int/float:största talet i listan 
    """
    
    max_tal = tal_lista[0]
    
    for tal in tal_lista:
        if tal > max_tal:
            max_tal = tal
    
    return max_tal  