#rate_monotonic_analysis
##This project is an implementation for:
##1- Bound Test: This test calculates the utilization of the tasks and checks if it is within the bound given by the Rate Monotonic Scheduling (RMS) bound formula U(n)=n(2^(1/n)−1).
##2- Completion Test: This test simulates the task execution to check if all tasks can be completed within their periods using a simple scheduling simulation.
##test cases:
##case 1:
##T1 = (12, 3),
##T2 = (15, 2),
##T3 = (30, 10).
##bound test succeded
##case 2:
##T1 = (10, 2.5),
##T2 = (20, 5),
##T3 = (30, 9).
##bound test failed but completion test succeeded
