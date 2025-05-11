from . import values

def process_cost(individual_number,seat_waste):
    if seat_waste != 0 :
        return individual_number * getattr(values,"DEFAULT_AMOUNT")
    
    return (individual_number-1) * getattr(values,"DEFAULT_AMOUNT")
     

def best_fit_table(tables,individuals_number):

    if individuals_number %2 == 1 :
        for table in tables:
            if table.seats == individuals_number:
                cost = process_cost(individuals_number,0) 
                return table,cost

        individuals_number +=1 
        
    minimum_waste = 10
    fit_table = None
    for table in tables:
        if table.seats >= individuals_number and (table.seats - individuals_number) < minimum_waste:
            minimum_waste = table.seats - individuals_number
            fit_table = table
            if minimum_waste == 0 :
                break

    if fit_table is not  None:
        cost = process_cost(individuals_number,minimum_waste)
        return fit_table,cost
    
    return None,None