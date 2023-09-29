function Dashboard(){
    return(
    <div>
        <div id="dashboardPage">
            <div id="dashboardRow1">
                <div className="dashboard" id="dashboard1">
                    <div className="title"># of recent walks</div>
                    <div className="info" ></div>
                </div>
                <span className="dashboard" id="dashboard2">
                    <div className="title" >Last Diary Entry</div>
                    <div className="info" > </div>
                <div id="inputDashboard2"></div>
                </span>
            </div>
            <div id="dashboardRow2">
                <span className="dashboard" id="dashboard3">
                        <div  className="title" >Hiro's Quote</div>
                        <div className="info" >
                        Simplicity is prerequisite for reliability. -Edsger W. Dijkstra, computer scientist 
                        </div>
                </span>
                <span className="dashboard" id="dashboard4">
                        <div className="title" >Average feeling</div>
                        <div className="info"></div>
                </span>
            </div>
        </div>
    </div>
    )
}

export default Dashboard