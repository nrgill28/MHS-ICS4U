'use strict';

// Some constants
const LIST_ROW_HEADER = "<tr><th>Name</th><th>Grade</th><th>Student Number</th><th>Actions</th></tr>";
const LIST_ROW_TEMPLATE = "<tr><td>{NAME}</td><td>{GRADE}</td><td>{SID}</td><td><a class=\"w3-button w3-green\" href=\"view.html?sid={SID}\"'>View</a>  <a class=\"w3-button w3-blue\" href=\"edit.html?sid={SID}\"'>Edit</a>  <a class=\"w3-button w3-red\" onclick='delete_user(\"{SID}\")'>Delete</a></td></tr>";

/**
 * This function gets list of users and populates the users list with them
 */
async function populate_list() {
    // Get and clear the table
    let table = document.getElementById("users-table");
    table.innerHTML = LIST_ROW_HEADER;

    // Define some parameters
    let params = getUrlParameters();
    let limit = parseInt(params['limit'] ?? -1);
    let currentPage = parseInt(params['page'] ?? 0);
    let offset = limit * currentPage;

    // Get the users
    let response = await eel.get_users(limit, offset)();
    let users = response.data;
    let total = response.total;

    console.log(users);

    // Update the table
    let max = total < offset + limit ? total : offset + limit;
    if (max === -1) max = total;
    for (let i = 0; i < max; i++) {
        // For each user, generate the table rows
        let user = users[i];
        let html = LIST_ROW_TEMPLATE.replace(/{NAME}/g, user.name);
        html = html.replace(/{GRADE}/g, user.grade);
        html = html.replace(/{SID}/g, user.sid);

        // Append the table row
        table.innerHTML += html;
    }
}

/**
 * This function deletes a user with the given Student ID
 * @param SID The Student ID
 */
async function delete_user(SID) {
    // Call the Python function responsible for this, wait for it to complete, then refresh
    await eel.delete_user(SID);
    await populate_list();
}

/**
 * This function returns a list of all the URL parameters there are.
 * @returns {{}} The parameters
 */
function getUrlParameters() {
    let vars = {};
    let parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

/**
 * This function will populate the edit values for the edit page
 */
async function populate_edit() {
    let params = getUrlParameters();
    let sid = params['sid'];

    // If it's a new user don't load anything
    if (sid !== "new") {
        // Otherwise get the user data and apply it
        let user = await eel.get_user(sid)();
        document.getElementById("edit-name").value = user.name;
        document.getElementById("edit-id").value = user.sid;
        document.getElementById("old-sid").value = user.sid;
        document.getElementById("edit-grade").value = user.grade;
        document.getElementById("edit-p1").value = user.courses.p1;
        document.getElementById("edit-p2").value = user.courses.p2;
        document.getElementById("edit-p3").value = user.courses.p3;
        document.getElementById("edit-p4").value = user.courses.p4;
        document.getElementById("edit-e1").value = user.courses.e1;
        document.getElementById("edit-e2").value = user.courses.e2;
        document.getElementById("edit-e3").value = user.courses.e3;
    }
}

/**
 * This function will save the values entered in the edit user page
 */
async function save_user() {
    // Bundle up all the data and send it off
    let user = {
        "name": document.getElementById("edit-name").value,
        "sid": document.getElementById("edit-id").value,
        "grade": document.getElementById("edit-grade").value,
        "courses": {
            "p1": document.getElementById("edit-p1").value,
            "p2": document.getElementById("edit-p2").value,
            "p3": document.getElementById("edit-p3").value,
            "p4": document.getElementById("edit-p4").value,
            "e1": document.getElementById("edit-e1").value,
            "e2": document.getElementById("edit-e2").value,
            "e3": document.getElementById("edit-e3").value,
        }
    };

    let sid = document.getElementById("old-sid").value;
    await eel.set_user(sid, user)();
    window.location = "/list.html";
}

/**
 * This function is used to populate the table in the view student page
 */
async function populate_table() {
    let name = document.getElementById("student-name");
    let sid = getUrlParameters()['sid'];

    let student = await eel.get_user(sid)();

    name.innerHTML = student.name + " (<span class='w3-text-grey'>" + student.sid + "</span>)";

    document.getElementById("period-1").innerHTML = student.courses.p1;
    document.getElementById("period-2").innerHTML = student.courses.p2;
    document.getElementById("period-3").innerHTML = student.courses.p3;
    document.getElementById("period-4").innerHTML = student.courses.p4;
    document.getElementById("extra-1").innerHTML = student.courses.e1;
    document.getElementById("extra-2").innerHTML = student.courses.e2;
    document.getElementById("extra-3").innerHTML = student.courses.e3;

}

/**
 * This is a work around for the issue in Eel where switching pages too quickly will kill it
 */
function unlock_buttons() {
    document.getElementById("navbar-home").href = "index.html";
    document.getElementById("navbar-list").href = "list.html";
    document.getElementById("button-new").href = "edit.html?sid=new";
}

setTimeout(unlock_buttons, 1000);