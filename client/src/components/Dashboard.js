function Dashboard(){
    return(
    <div>
        <div id="dashboardPage">
            <div id="dashboardRow1">
                <div className="dashboard" id="dashboard1">
                    <div>
                    <div id="testDashboard1">Test </div>
                    <div id="inputDashboard1">Test Text</div>
                    </div>
                </div>
                <span className="dashboard" id="dashboard2">
                <div>
                    <div id="testDashboard1">Test </div>
                    <div id="inputDashboard1">Test Text</div>
                </div>
                <div id="inputDashboard2"></div>
                </span>
            </div>
            <div id="dashboardRow2">
                <span className="dashboard" id="dashboard3">
                    <div>
                        <div id="testDashboard1">Test </div>
                        <div id="inputDashboard1">Test Text</div>
                    </div>
                </span>
                <span className="dashboard" id="dashboard4">
                    <div>
                        <div id="testDashboard1">Test </div>
                        <div id="inputDashboard1">Test Text</div>
                    </div>
                </span>
            </div>
        </div>
    </div>
    )
}

export default Dashboard