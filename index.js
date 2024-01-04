// Fetch JSON data from 'mainJSON.json'
fetch('mainJSON.json')
// Fetch JSON data from 'mainJSON.json'
.then(response => response.json())
.then(jsonData => {
    // Create a table
    const table = d3.select("#chart").append("table");

    // Append thead and tbody
    const thead = table.append("thead");
    const tbody = table.append("tbody");

    // Get column headers from the first entry
    const columns = ['Skin: ', ...Object.keys(jsonData[Object.keys(jsonData)[0]])];

    // Append the header row
    thead.append("tr")
        .selectAll("th")
        .data(columns)
        .enter()
        .append("th")
        .text(d => d);

    // Append the data rows
    const rows = tbody.selectAll("tr")
        .data(Object.entries(jsonData))
        .enter()
        .append("tr");

    // Append cells with data
    const cells = rows.selectAll("td")
        .data(d => {
            const title = d[0].toLowerCase().replace(/\s+/g, ' '); // Replace underscores with spaces
            return [title, ...Object.values(d[1])];
        })
        .enter()
        .append("td")
        .text(d => d);
})
.catch(error => console.error('Error fetching JSON:', error));