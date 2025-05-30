// forms_app/static/forms_app/scripts.js
$(document).ready(function () {
    let lastFormFields = [];

    function loadAttributes(type, name) {
        $.ajax({
            url: '/forms/fetch_data/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ type: type, name: name }),
            headers: {'X-CSRFToken': getCsrfToken()},
            dataType: 'json',
            success: function(data) {
                let content = $('#editor').empty();
                let fieldsList = $('#fields-list');
                
                if (type === 'formularze') {
                    content.append('<h3>Formularz: ' + name + '</h3>');
                    lastFormFields = Object.keys(data);
                    
                    fieldsList.empty();
                    lastFormFields.forEach(function(field) {
                        fieldsList.append(`<button class="field-btn" data-field="${field}">${field}</button>`);
                    });

                    $.each(data, function (key, value) {
                        content.append(`<div class='item'><span>${key}: ${value}</span>
<div class="buttons">
    <button class='move-up' data-type='${type}' data-name='${name}' data-attr='${key}'>↑</button>
    <button class='move-down' data-type='${type}' data-name='${name}' data-attr='${key}'>↓</button>
    <button class='delete' data-type='${type}' data-name='${name}' data-attr='${key}'>×</button>
</div>
</div>`);
                    });

                    content.append(`
                        <div id="add-field-form">
                            <input type="text" id="new-field-name" placeholder="Nazwa pola">
                            <input type="text" id="new-field-value" placeholder="Wartość">
                            <button id="add-field-btn" data-type="${type}" data-name="${name}">Dodaj pole</button>
                        </div>
                    `);
                } else {
                    content.append(`<h3>Szablon: ${name}</h3><textarea id='template-text'>${data.template_text}</textarea><br><button id='save-template' data-name='${name}'>Zapisz</button>`);
                }
            }
        });
    }

    function getCsrfToken() {
        return $('input[name="csrfmiddlewaretoken"]').val() || document.cookie.match(/csrftoken=([^;]+)/)[1];
    }

    $('.form-link, .template-link').click(function (e) {
        e.preventDefault();
        loadAttributes($(this).data('type'), $(this).data('name'));
    });

    $(document).on('click', '.field-btn', function() {
        let field = $(this).data('field');
        let textarea = $('#template-text');
        if (textarea.length) {
            let currentText = textarea.val();
            let newText = currentText + `{${field}}`;
            textarea.val(newText);
        }
    });

    $(document).on('click', '.delete, .move-up, .move-down', function () {
        let button = $(this);
        let type = button.data('type');
        let name = button.data('name');
        let attr = button.data('attr');
        let action = button.hasClass('delete') ? 'delete' : button.hasClass('move-up') ? 'move_up' : 'move_down';
        $.ajax({
            url: '/forms/api_action/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ action: action, type: type, name: name, attr: attr }),
            headers: {'X-CSRFToken': getCsrfToken()},
            success: function () {
                loadAttributes(type, name);
            }
        });
    });

    $(document).on('click', '#save-template', function () {
        let name = $(this).data('name');
        let text = $('#template-text').val();
        $.ajax({
            url: '/forms/api_action/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ action: 'save_template', type: 'szablony', name: name, value: text }),
            headers: {'X-CSRFToken': getCsrfToken()},
            success: function () {
                alert('Szablon zapisany!');
            }
        });
    });

    $(document).on('click', '#add-field-btn', function () {
        let type = $(this).data('type');
        let name = $(this).data('name');
        let attr = $('#new-field-name').val().trim();
        let value = $('#new-field-value').val().trim();

        if (attr && value) {
            $.ajax({
                url: '/forms/api_action/',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ action: 'add', type: type, name: name, attr: attr, value: value }),
                headers: {'X-CSRFToken': getCsrfToken()},
                success: function () {
                    loadAttributes(type, name);
                    $('#new-field-name').val('');
                    $('#new-field-value').val('');
                }
            });
        } else {
            alert('Wypełnij oba pola!');
        }
    });

    $('#download-json').click(function() {
        window.location.href = '/forms/download_json/';
    });
});