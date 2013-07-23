sitegraph-python
================

##Quick Start
    import sitegraph
    api = sitegraph.Api("YOUR AUTHENTICATION KEY")
    api.increment("statistic-identifier")
   
##Functions
###increment()
Increments a statistic by the given amount

	api.incremnet("identifier")

###decrement()
Decrements a statistic by the given amount

	api.decrement("identifier")	# Not specifying an amount assumes 1
	
	api.decrement("identifier", amount=10)

###create_event()
Creates a new event in the Sitegraph system. 

    api.create_event("Event Description")
    

##Support
If you're having problems with the library, drop us a line at support@sitegraph.net with your problem,
and we'll help you fix it!