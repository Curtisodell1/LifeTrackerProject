function Dashboard(){
    return(
    <div>
        <div>
            <div id="dashboardRow1">
                <div id="dashboard1">
                    <div>
                    <div id="testDashboard1">Test </div>
                    <div id="inputDashboard1">Test Text</div>
                    </div>
                </div>
                <span id="dashboard2">
                <div id="inputDashboard2">hi</div>
                </span>
            </div>
            <div >
                SPACED
                {/* Will need to make this as a determined border or 
                have padding on other divs */}
            </div>
            <div id="dashboardRow2">
                <span id="dashboard3">
                    <div id="inputDashboard3">Test Text</div>
                </span>
                <span id="dashboard4">
                <div id="inputDashboard4">hi</div>
                </span>
            </div>
        </div>
    </div>
    )
}

export default Dashboard