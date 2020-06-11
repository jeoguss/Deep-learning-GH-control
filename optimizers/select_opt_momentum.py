def setupOptimizer(net, device,  optimzer_select='NLLLoss'):
	if (optimzer_select == 'NLLLoss'):
		model =  net.to(device)
		criteria = nn.CrossEntropyLoss()
		optimizer = optim.SGD(model.parameters(), lr = 0.01, momentum=0.9)

	return optimizer
