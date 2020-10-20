<html>
<head>
	<title>DAY Tasks </title>
	<link rel="stylesheet" href="static/styles.css">

    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="static/script.js"></script>
    

    
</head>
<body>
	<div class="container">
    	<h1>Exsisted tasks [ {{ total_tasks }} ] </h1>
        <h2>Incompleted [ {{ incomplete }} ]</h2>
        <h3>Completed [ {{ complete }} ]
    		<ul id="todo-list" method="post">
    			% for task in tasks:
                    % if task.is_completed:
    			        <li class="completed">
    				        <input class="checkbox" data-uid={{ task.uid }} type="checkbox" disabled="disabled" checked="checked" />
                    % else:
                        <li>
                            <input class="checkbox" data-uid={{ task.uid }} type="checkbox"/>
                    % end
            			{{ task }}
    		          	<a class="remove" href= "api/delete/{{ task.uid }}">X</a>
                            </hr>
   				         </li>
   				 % end
    		</ul>
    		<form id="todo-add" action="/add-task" method="post">
    			<input type="text" id="new-todo-description" class="form-control" name="description"/>
    			<button class="add" type="submit">+</button>
    		</form>
    </div>
</body>
</html>