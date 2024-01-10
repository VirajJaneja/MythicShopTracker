// Fetch JSON data from 'mainJSON.json'
fetch('mainJSON.json')
    .then(response => response.json())
    .then(jsonData => {
        const table = d3.select("#chart").append("table").style("border", "1px solid #242c36"); 

        const thead = table.append("thead");
        const tbody = table.append("tbody");

        const excludedColumns = ['4th Appearance', '5th Appearanace']; 

        const columns = ['Skin: ', ...Object.keys(jsonData[Object.keys(jsonData)[0]]).filter(key => !excludedColumns.includes(key))];

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

                const updatedData = [formattedTitle, ...Object.values(d[1]).filter((value, index) => !excludedColumns.includes(Object.keys(d[1])[index]))].map(value => value === "0.0" ? "" : value);

                return updatedData;
            })
            .enter()
            .append("td")
            .text(d => d)
            .style("color", (d, i) => i === 0 ? "#D0A85C" : "white")
            .style("text-align", (d, i) => i === 0 ? "left" : "center");
    })
    .catch(error => console.error('Error fetching JSON:', error));
