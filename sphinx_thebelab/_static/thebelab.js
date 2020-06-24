/**
 * Add attributes to Thebelab blocks to initialize thebelab properly
 */

var initThebelab = () => {
    console.log("Adding thebelab to code cells...");

    // Load thebe config in case we want to update it as some point
    thebe_config = $('script[type="text/x-thebe-config"]')[0]

    // If Thebelab hasn't loaded, wait a bit and try again. This
    // happens because we load ClipboardJS asynchronously.
    if (window.thebelab === undefined) {
        setTimeout(addThebelabToCodeCells, 250)
    return
    }

    // If we already detect a Thebelab cell, don't re-run
    if (document.querySelectorAll('div.thebelab-cell').length > 0) {
        return;
    }

    // Update thebelab buttons with loading message
    $(".thebelab-launch-button").each((ii, button) => {
        button.innerHTML = `
        <div class="spinner">
            <div class="rect1"></div>
            <div class="rect2"></div>
            <div class="rect3"></div>
            <div class="rect4"></div>
        </div>
        <span class="loading-text"></span>`;
    })

    // Set thebelab event hooks
    thebelab.on("status", function (evt, data) {
        console.log("Status changed:", data.status, data.message);
        $(".thebelab-launch-button ")
        .attr("class", "thebelab-button thebelab-launch-button thebe-status-" + data.status)
        .find(".loading-text").html("Launching from mybinder.org: <span class='status'>" + data.status + "</span>");

        // Find any cells with an initialization tag and ask ThebeLab to run them when ready
        if (data.status === "ready") {
            var thebeInitCells = document.querySelectorAll('.thebelab-init');
            thebeInitCells.forEach((cell) => {
                console.log("Initializing ThebeLab with cell: " + cell.id);
                cell.querySelector('.thebelab-run-button').click();
            });
        }
    });


    // Find all code cells, replace with Thebelab interactive code cells
    const codeCells = document.querySelectorAll(thebelab_selector)
    codeCells.forEach((codeCell, index) => {
        const codeCellId = index => `codecell${index}`;
        codeCell.id = codeCellId(index);
        codeCellText = codeCell.querySelector(thebelab_selector_code);
        codeCellOutput = codeCell.querySelector(thebelab_selector_output);

        // Clean up the language to make it work w/ CodeMirror and add it to the cell
        dataLanguage = detectLanguage(kernelName);

        if (codeCellText) {
            codeCellText.setAttribute('data-language', dataLanguage);
            codeCellText.setAttribute('data-executable', 'true');

            // If we had an output, insert it just after the `pre` cell
            if (codeCellOutput) {
                $(codeCellOutput).attr("data-output", "");
                $(codeCellOutput).insertAfter(codeCellText);
            }
        }
    });

    // Init thebelab
    thebelab.bootstrap();
}

// Helper function to munge the language name
var detectLanguage = (language) => {
    if (language.indexOf('python') > -1) {
        language = "python";
    } else if (language === 'ir') {
        language = "r"
    }
    return language;
}
