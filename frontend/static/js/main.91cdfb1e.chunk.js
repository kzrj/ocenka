(this.webpackJsonpocenka=this.webpackJsonpocenka||[]).push([[0],{13:function(e,t,n){"use strict";n.r(t),n.d(t,"JobsTypes",(function(){return d})),n.d(t,"INITIAL_STATE",(function(){return g})),n.d(t,"JobsSelectors",(function(){return f})),n.d(t,"getJobsRequest",(function(){return b})),n.d(t,"getJobsSuccess",(function(){return m})),n.d(t,"getJobsFail",(function(){return p})),n.d(t,"getJobDetailRequest",(function(){return E})),n.d(t,"getJobDetailSuccess",(function(){return h})),n.d(t,"getJobDetailFail",(function(){return O})),n.d(t,"getCategoriesRequest",(function(){return v})),n.d(t,"getCategoriesSuccess",(function(){return j})),n.d(t,"getCategoriesFail",(function(){return T})),n.d(t,"reducer",(function(){return k}));var a,r=n(8),c=n(31),o=n(52),s=n.n(o),u=Object(c.createActions)({getJobsRequest:["payload"],getJobsFail:["payload"],getJobsSuccess:["payload"],getJobDetailRequest:["payload"],getJobDetailFail:["error"],getJobDetailSuccess:["payload"],getCategoriesRequest:["payload"],getCategoriesFail:["payload"],getCategoriesSuccess:["payload"]}),l=u.Types,i=u.Creators,d=l;t.default=i;var g=s()({listFetching:!1,jobs:[],categories:[],errorList:null,detailFetching:null,jobDetail:null,errorDetail:null,message:""}),f={getJobs:function(e){return e.jobs.job_list},getCategories:function(e){return e.jobs.categories}},b=function(e,t){t.payload;return e.merge({listFetching:!0,jobs:[]})},m=function(e,t){var n=t.payload;return e.merge({listFetching:!1,errorList:null,jobs:n})},p=function(e,t){var n=t.payload;return e.merge({listFetching:!1,errorList:n,jobs:[]})},E=function(e,t){t.payload;return e.merge({detailFetching:!0})},h=function(e,t){var n=t.payload;return e.merge({detailFetching:!1,errorDetail:null,jobDetail:n})},O=function(e,t){var n=t.error;return e.merge({detailFetching:!1,errorDetail:n,jobDetail:null})},v=function(e,t){t.payload;return e.merge({listFetching:!0,categories:[]})},j=function(e,t){var n=t.payload;return e.merge({listFetching:!1,errorList:null,categories:n})},T=function(e,t){var n=t.payload;return e.merge({listFetching:!1,errorList:n,categories:[]})},k=Object(c.createReducer)(g,(a={},Object(r.a)(a,l.GET_JOBS_REQUEST,b),Object(r.a)(a,l.GET_JOBS_SUCCESS,m),Object(r.a)(a,l.GET_JOBS_FAIL,p),Object(r.a)(a,l.GET_JOB_DETAIL_REQUEST,E),Object(r.a)(a,l.GET_JOB_DETAIL_SUCCESS,h),Object(r.a)(a,l.GET_JOB_DETAIL_FAIL,O),Object(r.a)(a,l.GET_CATEGORIES_REQUEST,v),Object(r.a)(a,l.GET_CATEGORIES_SUCCESS,j),Object(r.a)(a,l.GET_CATEGORIES_FAIL,T),a))},254:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),c=n(48),o=n.n(c),s=n(28),u=n(7),l=n(21),i=n(19),d=n(95),g=n(98),f=n(10),b=n.n(f),m=n(5),p=n(22),E=n.n(p),h="".concat("https://34.66.36.82","/api"),O={JWT_AUTH:"".concat(h,"/jwt/api-token-auth/"),JWT_CHECK_TOKEN:"".concat(h,"/jwt/api-token-verify/"),SIGNUP:"".concat(h,"/users/"),GET_JOBS:"".concat(h,"/jobs/"),getJobDetail:function(e){return"".concat(h,"/jobs/").concat(e,"/")},GET_CATEGORIES:"".concat(h,"/categories/")},v=function(e){if(e&&"undefined"!==typeof e.response){var t={status:e.response.status,statusText:e.response.statusText,message:null,response:e.response};if("message"in e.response.data)t.message=JSON.stringify(e.response.data.message);else{var n="";for(var a in e.response.data)n+="".concat(a,": ").concat(e.response.data[a],". ");t.message=n}return t}return{status:"Connection Error",statusText:"An error occurred while sending your data!",message:"An error occurred while sending your data!"}},j=function(e){var t=new URLSearchParams;return null!=e&&Object.keys(e).forEach((function(n){null===e[n]||e[n]instanceof Array||t.append(n,e[n]),null!==e[n]&&e[n]instanceof Array&&(delete t[n],e[n].map((function(e){return""!==e&&t.append(n,e),null})))})),t},T=function(){return{logIn:function(e){var t=e.username,n=e.password;return E.a.post(O.JWT_AUTH,{username:t,password:n}).then((function(e){if(e.status<200||e.status>=300)throw new Error(e);return{token:e.data.token,user:e.data.user}})).catch((function(e){throw new Error(e.response.data[Object.keys(e.response.data)[0]][0])})).then((function(e){return localStorage.setItem("token",e.token),e.user}))},checkToken:function(e){return E.a.post(O.JWT_CHECK_TOKEN,{token:e}).then((function(e){return localStorage.setItem("token",e.data.token),e.data})).catch((function(e){var t=new Error(e);throw t.data=v(e),t}))},logOut:function(){localStorage.removeItem("token")}}},k=function(){return{getJobs:function(e){var t=j(e);return E.a.get(O.GET_JOBS,{params:t}).then((function(e){return e.data})).catch((function(e){var t=new Error(e);throw t.data=v(e),t}))},getCategories:function(e){var t=j(e);return E.a.get(O.GET_CATEGORIES,{params:t}).then((function(e){return e.data})).catch((function(e){var t=new Error(e);throw t.data=v(e),t}))},getJobDetail:function(e){localStorage.getItem("token");var t=O.getJobDetail(e);return E()({method:"get",url:t}).then((function(e){return e.data})).catch((function(e){var t=new Error(e);throw t.data=v(e),t}))}}},S=n(9),_=n(13),I=b.a.mark(L),y=b.a.mark(J),C=b.a.mark(N);function L(e,t){var n,a;return b.a.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return n=t.data,r.next=3,Object(m.c)(S.default.resetAuthErrors());case 3:return r.prev=3,r.next=6,Object(m.b)(e.logIn,n);case 6:return a=r.sent,r.next=9,Object(m.c)(S.default.loginSuccess(a));case 9:return r.next=11,Object(m.c)(S.default.toggleModal(!1));case 11:r.next=17;break;case 13:return r.prev=13,r.t0=r.catch(3),r.next=17,Object(m.c)(S.default.loginFailure(r.t0.message));case 17:case"end":return r.stop()}}),I,null,[[3,13]])}function J(e,t){return b.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,Object(m.b)(e.logOut);case 3:return t.next=5,Object(m.c)(S.default.logoutSuccess());case 5:t.next=11;break;case 7:return t.prev=7,t.t0=t.catch(0),t.next=11,Object(m.c)(S.default.logoutFailure(t.t0.message));case 11:case"end":return t.stop()}}),y,null,[[0,7]])}function N(e,t){var n,a;return b.a.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return n=t.payload,r.prev=1,r.next=4,Object(m.b)(e.checkToken,n);case 4:return a=r.sent,r.next=7,Object(m.c)(S.default.checkTokenSuccess(a));case 7:r.next=13;break;case 9:return r.prev=9,r.t0=r.catch(1),r.next=13,Object(m.c)(S.default.checkTokenFail(r.t0.message));case 13:case"end":return r.stop()}}),C,null,[[1,9]])}var x=b.a.mark(F),R=b.a.mark(A),w=b.a.mark(G);function F(e,t){var n;return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return a.prev=0,a.next=3,Object(m.b)(e.getJobs,t.payload);case 3:return n=a.sent,a.next=6,Object(m.c)(_.default.getJobsSuccess(n.results));case 6:a.next=12;break;case 8:return a.prev=8,a.t0=a.catch(0),a.next=12,Object(m.c)(_.default.getJobsFail(a.t0));case 12:case"end":return a.stop()}}),x,null,[[0,8]])}function A(e,t){var n;return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return a.prev=0,a.next=3,Object(m.b)(e.getJobDetail,t.payload);case 3:return n=a.sent,a.next=6,Object(m.c)(_.default.getJobDetailSuccess(n));case 6:a.next=12;break;case 8:return a.prev=8,a.t0=a.catch(0),a.next=12,Object(m.c)(_.default.getJobDetailFail(a.t0));case 12:case"end":return a.stop()}}),R,null,[[0,8]])}function G(e,t){var n;return b.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return a.prev=0,a.next=3,Object(m.b)(e.getCategories,t.payload);case 3:return n=a.sent,a.next=6,Object(m.c)(_.default.getCategoriesSuccess(n.results));case 6:a.next=12;break;case 8:return a.prev=8,a.t0=a.catch(0),a.next=12,Object(m.c)(_.default.getCategoriesFail(a.t0));case 12:case"end":return a.stop()}}),w,null,[[0,8]])}var U=b.a.mark(K),D=T(),q=k();function K(){return b.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(m.a)([Object(m.d)(S.AuthTypes.LOGIN_REQUEST,L,D),Object(m.d)(S.AuthTypes.LOGOUT_REQUEST,J,D),Object(m.d)(S.AuthTypes.CHECK_TOKEN_REQUEST,N,D),Object(m.d)(_.JobsTypes.GET_JOBS_REQUEST,F,q),Object(m.d)(_.JobsTypes.GET_JOB_DETAIL_REQUEST,A,q),Object(m.d)(_.JobsTypes.GET_CATEGORIES_REQUEST,G,q)]);case 2:case"end":return e.stop()}}),U)}var Q=n(256),B=Object(i.combineReducers)({auth:n(9).reducer,jobs:n(13).reducer,form:Q.a}),M=n(26),H=n(27),z=n(30),W=n(29);function P(e){var t=e.job;return r.a.createElement("div",{className:"job-block"},r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-8"},r.a.createElement("a",{href:"",className:"job-title"},t.title)),r.a.createElement("div",{className:"col-4"},r.a.createElement("p",{className:"job-budget"},t.budget,"\u0440"))),r.a.createElement("p",{className:"job-description"},t.description),r.a.createElement("p",{className:"job-address"},t.address),r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-6"},r.a.createElement("p",{className:"job-zakazchik"},t.zakazchik)),r.a.createElement("div",{className:"col-6"},r.a.createElement("p",{className:"job-created-ago"},t.created_ago))))}var X=function(e){Object(z.a)(n,e);var t=Object(W.a)(n);function n(e){var a;return Object(M.a)(this,n),(a=t.call(this,e)).state={},a}return Object(H.a)(n,[{key:"componentDidMount",value:function(){this.props.getJobs()}},{key:"render",value:function(){var e=this.props.state.jobs,t=e.jobs,n=(e.categories,e.listFetching);e.errorList;return r.a.createElement("div",{className:"container-fluid "},r.a.createElement("div",{className:""},r.a.createElement("div",{className:"block-subscription"},r.a.createElement("button",{className:"btn"},"\u041f\u043e\u0434\u043f\u0438\u0441\u0430\u0442\u044c\u0441\u044f")),r.a.createElement("div",{className:"block-categories"},r.a.createElement("div",{className:"clearfix"})),r.a.createElement("div",{className:"jobs-block"},n&&r.a.createElement("p",null,"Loading..."),t.length>0&&t.map((function(e){return r.a.createElement(P,{job:e})})))))}}]),n}(a.Component),V=Object(l.b)((function(e){return{notifications:e.notifications,state:e}}),(function(e){return{getCategories:function(t){return e(_.default.getCategoriesRequest(t))},getJobs:function(t){return e(_.default.getJobsRequest(t))}}}))(X),Y=function(e){Object(z.a)(n,e);var t=Object(W.a)(n);function n(){return Object(M.a)(this,n),t.apply(this,arguments)}return Object(H.a)(n,[{key:"componentDidMount",value:function(){var e=this.props.match.params.token;console.log(this.props.state),e&&this.props.checkToken(e)}},{key:"render",value:function(){var e=!1;return!0===this.props.isLoggedIn&&(e=!0),r.a.createElement("div",null,e?r.a.createElement(V,null):"\u041d\u0435 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u043d")}}]),n}(a.Component),Z=Object(l.b)((function(e){return{isLoggedIn:e.auth.isLoggedIn,user:e.auth.user,state:e}}),(function(e){return{checkToken:function(t){return e(S.default.checkTokenRequest(t))}}}))(Y);function $(e){return r.a.createElement("div",{className:"modal fade",id:"authModal",tabindex:"-1",role:"dialog","aria-labelledby":"authModalLabel","aria-hidden":"true"},r.a.createElement("div",{className:"modal-dialog"},r.a.createElement("div",{className:"modal-content"},r.a.createElement("div",{className:"modal-header"},r.a.createElement("h5",{className:"modal-title",id:"authModalLabel"},"\u0412\u043e\u0439\u0442\u0438 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e"),r.a.createElement("button",{type:"button",className:"close","data-dismiss":"modal","aria-label":"Close"},r.a.createElement("span",{"aria-hidden":"true"},"\xd7"))),r.a.createElement("div",{className:"modal-body"},r.a.createElement("a",{href:"viber://pa?chatURI=dm-eda&context=Chto_za_CONTEXT?&text=\u0432\u043e\u0439\u0442\u0438"},"\u0412\u043e\u0439\u0442\u0438 \u0447\u0435\u0440\u0435\u0437 \u0432\u0430\u0439\u0431\u0435\u0440")))))}var ee=function(e){Object(z.a)(n,e);var t=Object(W.a)(n);function n(e){var a;return Object(M.a)(this,n),(a=t.call(this,e)).state={},a}return Object(H.a)(n,[{key:"componentDidMount",value:function(){var e=localStorage.getItem("token");e&&this.props.checkToken(e)}},{key:"render",value:function(){var e=this.props.auth,t=e.isLoggedIn,n=e.user;return r.a.createElement("div",{className:"header"},r.a.createElement("h4",{className:"head-title"},"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430"),t?n.zakazchik?r.a.createElement("div",null,r.a.createElement(s.b,{to:"/dm/shops/create/"},"\u041c\u043e\u0438 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f"),r.a.createElement("p",null,n.viber_name," ",r.a.createElement("button",{onClick:this.props.logout},"\u0412\u044b\u0439\u0442\u0438"))):r.a.createElement("div",null,r.a.createElement(s.b,{to:"/dm/shops/create/"},"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0431\u044c\u044f\u0432\u043b\u0435\u043d\u0438\u0435"),r.a.createElement("p",null,n.viber_name," ",r.a.createElement("button",{onClick:this.props.logout},"\u0412\u044b\u0439\u0442\u0438"))):r.a.createElement("div",null,r.a.createElement("button",{className:"btn","data-toggle":"modal","data-target":"#authModal"},"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0431\u044c\u044f\u0432\u043b\u0435\u043d\u0438\u0435"),r.a.createElement("button",{className:"btn","data-toggle":"modal","data-target":"#authModal"},"\u0412\u043e\u0439\u0442\u0438")),r.a.createElement($,null),r.a.createElement("hr",null))}}]),n}(a.Component),te=Object(l.b)((function(e){return{auth:e.auth,state:e}}),(function(e){return{checkToken:function(t){return e(S.default.checkTokenRequest(t))},logout:function(){return e(S.default.logoutRequest())}}}))(ee),ne=function(e){var t=Object(g.a)(),n=Object(i.createStore)(B,Object(d.composeWithDevTools)(Object(i.applyMiddleware)(t)));t.run(K);return n}();o.a.render(r.a.createElement(l.a,{store:ne},r.a.createElement(s.a,null,r.a.createElement("div",{classname:"app"},r.a.createElement(te,null),r.a.createElement(u.c,null,r.a.createElement(u.a,{exact:!0,path:"/"},r.a.createElement(V,null)),r.a.createElement(u.a,{path:"/dm/login/v/:token",component:Z})),r.a.createElement("div",{className:"footer"},r.a.createElement("p",{className:"foot-title"},"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0438\u0441\u0430"))))),document.getElementById("root"))},9:function(e,t,n){"use strict";n.r(t),n.d(t,"AuthTypes",(function(){return d})),n.d(t,"INITIAL_STATE",(function(){return g})),n.d(t,"AuthSelectors",(function(){return f})),n.d(t,"loginRequest",(function(){return b})),n.d(t,"loginSuccess",(function(){return m})),n.d(t,"loginFailure",(function(){return p})),n.d(t,"logoutRequest",(function(){return E})),n.d(t,"logoutSuccess",(function(){return h})),n.d(t,"logoutFailure",(function(){return O})),n.d(t,"checkTokenRequest",(function(){return v})),n.d(t,"checkTokenSuccess",(function(){return j})),n.d(t,"checkTokenFail",(function(){return T})),n.d(t,"reducer",(function(){return k}));var a,r=n(8),c=n(31),o=n(52),s=n.n(o),u=Object(c.createActions)({loginRequest:["data"],loginSuccess:["user"],loginFailure:["error"],logoutRequest:null,logoutSuccess:null,logoutFailure:["error"],checkTokenRequest:["payload"],checkTokenSuccess:["payload"],checkTokenFail:["error"]}),l=u.Types,i=u.Creators,d=l;t.default=i;var g=s()({fetching:!1,user:null,error:"",isLoggedIn:!1,isLoggingIn:!1}),f={getUser:function(e){return e.user}},b=function(e,t){t.data;return e.merge({fetching:!0,user:null,isLoggingIn:!0,isLoggedIn:!1})},m=function(e,t){var n=t.user;return e.merge({fetching:!1,error:null,user:n,isLoggedIn:!0,isLoggingIn:!1})},p=function(e,t){var n=t.error;return e.merge({fetching:!1,error:n,user:null,isLoggedIn:!1,isLoggingIn:!1})},E=function(e){return e.merge({fetching:!0,isLoggingIn:!0})},h=function(e){return e.merge({fetching:!1,error:null,user:null,isLoggingIn:!1,isLoggedIn:!1})},O=function(e,t){var n=t.error;return e.merge({fetching:!1,error:n,isLoggingIn:!1})},v=function(e,t){t.payload;return e.merge({fetching:!0})},j=function(e,t){var n=t.payload;return e.merge({fetching:!1,error:null,user:n.profile,isLoggedIn:!0,isLoggingIn:!1})},T=function(e,t){var n=t.error;return e.merge({fetching:!1,error:n,user:null,isLoggedIn:!1,isLoggingIn:!1})},k=Object(c.createReducer)(g,(a={},Object(r.a)(a,l.LOGIN_REQUEST,b),Object(r.a)(a,l.LOGIN_SUCCESS,m),Object(r.a)(a,l.LOGIN_FAILURE,p),Object(r.a)(a,l.CHECK_TOKEN_REQUEST,v),Object(r.a)(a,l.CHECK_TOKEN_FAIL,T),Object(r.a)(a,l.CHECK_TOKEN_SUCCESS,j),Object(r.a)(a,l.LOGOUT_REQUEST,E),Object(r.a)(a,l.LOGOUT_SUCCESS,h),Object(r.a)(a,l.LOGOUT_FAILURE,O),a))},99:function(e,t,n){e.exports=n(254)}},[[99,1,2]]]);
//# sourceMappingURL=main.91cdfb1e.chunk.js.map