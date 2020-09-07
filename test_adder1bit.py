from adder1bit import calculation1bit

def test_calculation():
	assert (calculation(0, 0) == 0) #minimum value, passes 
	assert (calculation(0, 1) == 27) #normal value, passes
	assert (calculation(0, 1) == 27) #normal value, passes
	assert (calculation(1, 1) == 2) #maximum value, passes
	assert (calculation('string', 45)) #must fail
	assert (calculation(0.5, 0.7) == 1.2) #must fail
	assert (calculation(-1, 1) == 0) #must fail