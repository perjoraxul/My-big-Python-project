def call_functions_ma(ma_comparison_values,ma_list) :

	def ma_higher_lower_count(ma_comparison_values,ma_list) :
		higher = 0
		lower = 0
		equal = 0
		for _ in range(len(ma_comparison_values)) :
			if ma_comparison_values[_] > ma_list[_] :
				higher += 1
			elif ma_comparison_values[_] < ma_list[_] :
				lower += 1
			else : 
				equal += 1     
	  
		print(f"We have {higher} times the next goal was above the last moving average. ")
		print(f"We have {lower} times the next goal was below the last moving average. ")      
		print(f"We have {equal} times the next goal was the same as the last moving average. ")
		higher_ratio = higher/(higher+lower+equal) 
		lower_ratio = lower/(higher+lower+equal) 
		equal_ratio =  equal/(higher+lower+equal)    
		print(f"We have higher_ratio {higher_ratio}, lower_ratio {lower_ratio},equal_ratio {equal_ratio}")
		return higher,lower,equal        

	def ma_higher_lower_consecutive(ma_comparison_values,ma_list) :
		higher = 0
		lower = 0
		equal = 0
		higher_list = []
		lower_list = []
		equal_list = []

		for _ in range(len(ma_comparison_values)) :
			if ma_comparison_values[_] > ma_list[_] :
				higher += 1
				lower = 0
				equal = 0 
				higher_list.append(higher)	
			elif ma_comparison_values[_] < ma_list[_] :
				lower += 1
				higher = 0
				equal = 0 
				lower_list.append(lower)
			else : 
				equal += 1
				higher = 0
				lower = 0
				equal_list.append(equal)

			if equal_list == [] : 
				equal_list.append(0)
		print(f"We have a maximum of {max(higher_list)} times consecutive the next goal was above the last moving average. ")
		print(f"We have a maximum of {max(lower_list)} times consecutive the next goal was below the last moving average. ")      
		print(f"We have a maximum of {max(equal_list)} times consecutive the next goal was the same as the last moving average. ")     

		return max(higher_list),max(lower_list),max(equal_list)       

	
	return ma_higher_lower_count(ma_comparison_values,ma_list),ma_higher_lower_consecutive(ma_comparison_values,ma_list) 


