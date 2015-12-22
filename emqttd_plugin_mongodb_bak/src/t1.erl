-module(t1).

-export([start/0]).

start()->
	application:start(bson),
	application:start(crypto),
	application:start(mongodb),
	
	Database = <<"db0">>,
	{ok, Connection} = mongo:connect([{database, Database}]),
	MqttUser = #{
			   	<<username>> 	=> "10000",
				<<password>> 	=> "",
				<<salt>> 		=> "",
				<<created>> 	=> ""
			  },
	MqttAcl = #{
			   	<<allow>> 		=> "10000",%% Int 0: deny, 1: allow
				<<ipaddr>> 		=> "",%% String 
				<<username>> 	=> "",%% String 
				<<clientid>> 	=> "",%% String 
				<<access>> 		=> "",%% Int
				<<topic>> 		=> ""%% String 
			   },
	Message = [#{<<"name">> => unicode:characters_to_binary("稳不稳，！！！！"),
				 <<"desc">> => unicode:characters_to_binary("稳不稳，！！！！"),
				 <<"type">> => 18,
				 <<"time">> => 121325555555555555
			   },
			   #{<<"name">> => unicode:characters_to_binary("稳不�?1232131231，！！！�?"),
				<<"desc">> => unicode:characters_to_binary("稳不�?23123123123123，！！！�?"),
				<<"type">> => 1,
				<<"time">> => 7758521
			   }],
	Message1 = [{<<"name">>, unicode:characters_to_binary("稳不稳，！！！！"), <<"desc">>, <<"77777fuck">>, <<"sex">>, 17}],
	mongo:insert(Connection, <<"User">>, Message),
	
	Cursor = mongo:find(Connection, <<"config">>, {}),
	Result = mc_cursor:rest(Cursor),
	mc_cursor:close(Cursor),

	Map = lists:nth(1, Result),
	{ok,Value} = maps:find(<<"XMPPDomain">>, Map),
	Value.

%% 	-spec connect(database(), bson:utf8(), bson:utf8(), write_mode(), read_mode(), proplists:proplist()) -> {ok, pid()}.
%% 	{ok, Connection} = mongo:connect([{database, Database},{host,{Host,27017}}]).
%% 	{ok, Connection} = mongo:connect([{database, Database}]),
%% 	{ok, Connection} = mongo:connect([{host, Host},{login,<<"vchat">>},{password,<<"123456">>},{database, Database},{w_mode, safe}]),	
%% 	{ok, Connection} = mongo:connect([{host, Host}, {login,<<"vchat">>},{password,<<"123456">>},{database, Database},{w_mode, safe}]),	
%% 	mongo:connect({"db_name", "account", "password", "safe", "master", [{"host", Host}, {"port", 27017}]}),
%% 	Cursor = mongo:find(Connection, <<"UserAccount">>, {}),
%% 	Result = mc_cursor:rest(Cursor).
%% 	{ok, Pool} = mc_worker:start_link([{database,Database}]).
%%  {ok, Pool} = mc_worker:start_link([{host,Host}, {login, <<"vchat">>},  {password, <<"123456">>}, {database, Database}, {w_mode, safe}]).