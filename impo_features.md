# Important Features of an Issue Tracking Website

## User authentication and authorization

This feature allows users to create accounts and log into the website, and also assigns them different levels of access and permissions.

## Issue tracking

This is the core feature of the website and allows users to report and track issues, such as bugs or feature requests.

## Commenting and collaboration

This feature allows users to add comments to issues and collaborate with other users to resolve them.

## Dashboard

This feature allows users to track the progress of their issues, and to get a quick overview of all issues in the system.

## Reports

This feature allows users to generate and view reports on the status of all issues, and on the performance of the system over time.

## Notifications and email updates

This feature sends notifications to users when an issue is updated, and also sends email updates when an issue is assigned or resolved.

## Search and filtering

This feature allows users to search for and filter issues by various criteria, such as status, priority, and assigned user.

# User Stories

## User-Story-1
    1. Der User öffnet das Web-Frontend des Issue Trackers und gelangt auf die Seite zum Erstellen einer neuen Issue.
    2. Der User gibt eine beschreibende Überschrift und eine ausführliche Beschreibung der Issue in das Formular ein.
    3. Der User sendet das ausgefüllte Formular an das Django-Backend.
    4. Das Backend validiert die eingegebenen Daten (z.B. Überschrift darf nicht leer sein).
    5. Wenn die Daten gültig sind, werden sie in der Datenbank gespeichert und die Issue erhält eine eindeutige ID.
    6. Der User kann die Details der Issue aufrufen, bearbeiten oder löschen, indem er auf die entsprechenden Schaltflächen im Frontend klickt und die Anfrage an das Backend sendet.
    7. Das Backend ruft die entsprechenden Daten aus der Datenbank ab und sendet sie zur Anzeige im Frontend zurück.

## User-Story-2
    1. Der Entwickler öffnet das Web-Frontend des Issue Trackers und gelangt auf die Seite zur Anzeige der offenen Issues.
    2. Der Entwickler sortiert die Liste der Issues nach Priorität oder Erstellungsdatum.
    3. Der Entwickler klickt auf die ID einer bestimmten Issue, um die Details anzuzeigen.
    4. Das Backend ruft die Daten der ausgewählten Issue aus der Datenbank ab und sendet sie zur Anzeige im Frontend zurück.
