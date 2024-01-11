// Fetch JSON data from 'mainJSON.json'
fetch('mainJSON.json')
    .then(response => response.json())
    .then(jsonData => {
        const table = d3.select("#chart").append("table").style("border", "1px solid #242c36"); 

        const thead = table.append("thead");
        const tbody = table.append("tbody");

        const excludedColumns = ['4th Appearance', '5th Appearanace']; 

        const columns = ['Skin: ', ...Object.keys(jsonData[Object.keys(jsonData)[0]]).filter(key => !excludedColumns.includes(key))];
        const dateCol = 'Next Eligible:'
        columns.push(dateCol);
        thead.append("tr")
            .selectAll("th")
            .data(columns)
            .enter()
            .append("th")
            .text(d => d)
            .style("color", (d, i) => i === 0 ? "#D0A85C" : "#D0A85C");

        const rows = tbody.selectAll("tr")
            .data(Object.entries(jsonData))
            .enter()
            .append("tr");

        const cells = rows.selectAll("td")
            .data(d => {
                const title = d[0].toLowerCase().replace(/\s+/g, ' ');
                const formattedTitle = title.charAt(0).toUpperCase() + title.slice(1);
                const newDateValue = calculateDate(d); 
                const updatedData = [formattedTitle, ...Object.values(d[1]).filter((value, index) => !excludedColumns.includes(Object.keys(d[1])[index])), calculateDate(d)].map(value => value === "0.0" ? "" : value);
                return updatedData;
            })
            .enter()
            .append("td")
            .text(d => d)
            .style("color", (d, i) => i === 0 ? "#D0A85C" : "white")
            .style("text-align", (d, i) => i === 0 ? "left" : "center");
    })
    .catch(error => console.error('Error fetching JSON:', error));

    // const div1Height = document.getElementById('chart').offsetHeight;
    // document.getElementById('footer').style.marginTop = div1Height + 'px';


    // const tableHeight = document.getElementById('chart').offsetHeight;

    // document.getElementById('additionalDiv').style.height = tableHeight + 'px';


async function calculateDate(data) {
    const excludedColumns = ['4th Appearance', '5th Appearanace', 'Total Appearances'];
    const appearancesList = Object.entries(data[1]).filter(([key]) => !excludedColumns.includes(key)).map(([key, value]) => value);

    const patch = appearancesList.reduce((maxValue, currentValue) => {
        return currentValue.localeCompare(maxValue) > 0 ? currentValue : maxValue;
    }, '0.0');

    let resultDate = "ISNT WORKING";

    try {
        const response = await fetch('patchDates.json');
        const jsonData = await response.json();

        const temp = patch + '';
        const matchingObject = jsonData.find(obj => obj.patch === temp);

        if (matchingObject) {
            const correspondingDate = matchingObject.date;
            resultDate = correspondingDate;
        } else {
            console.log("ISSUE WITH DATA: " + data);
            return "Failed Process";
        }


        const currentDate = new Date(resultDate);

        currentDate.setFullYear(currentDate.getFullYear() + 1);

        const updatedDateString = currentDate.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });

        return updatedDateString;
    } catch (error) {
        console.error('Error fetching JSON:', error);
        return "Failed Process";
    }
}