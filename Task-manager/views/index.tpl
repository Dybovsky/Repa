<html>
<head>
	<title>DAY Tasks </title>
	<link rel="stylesheet" href="static/styles.css">

    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="static/script.js"></script>
    

    
</head>
<body>
	<div class="container">
        % if complete != 0:
    	<h1>Exsisted tasks [ {{ total_tasks }} ] </h1>
        <h2>Incompleted [ {{ incomplete }} ]</h2>
        <h3>Completed [ {{ complete }} ]
           % else:
           <h1>Exsisted tasks [ {{ total_tasks }} ] </h1>
        % end
    		<ul id="todo-list" >
    			% for task in tasks:
                    % if task.is_completed:
    			        <li class="completed" href="/api/complete/{{ task.uid }}">
    				        <input class="checkbox" data-uid={{ task.uid }} type="checkbox" disabled="disabled" checked="checked" />
                    % else:
                        <li>
                            <input class="checkbox" data-uid={{ task.uid }} type="checkbox"/>
                    % end
            			{{ task }}
    		          	<a class="remove" href= "api/delete/{{ task.uid }}">X</a>
                            <hr/>
   				         </li>
   				 % end
    		</ul>
            % if total_tasks <= 9:
    		<form id="todo-add" action="/add-task" method="post">
    			<input type="text" id="new-todo-description" class="form-control" name="description"/>
    			<button class="add" type="submit">+</button>
    		</form>
            % else:
             <h1>Finish other tasks, bro ... only 10 avalibale</h1>
            % end
    </div>
</body>
</html>