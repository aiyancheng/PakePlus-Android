/* ═══════════════════════════════════════════
   永州爱眼城 · 门店新员工培训配套工具模板
   公共脚本（tool-common.js）
   功能：所有输入框自动本地保存 / 一键清空 / 导出文本 / 打印
   ═══════════════════════════════════════════ */
(function(){
  'use strict';
  var PAGE = document.body.getAttribute('data-page') || 'tool';
  var KEY = 'eye8w_tool_' + PAGE + '_v1';

  /* ── 恢复与保存 ── */
  function collect(){
    var data = {};
    document.querySelectorAll('[data-save]').forEach(function(el){
      var id = el.getAttribute('data-save');
      if(el.type === 'checkbox'){ data[id] = el.checked; }
      else { data[id] = el.value; }
    });
    // 三态按钮
    document.querySelectorAll('.tri').forEach(function(g){
      var gid = g.getAttribute('data-tri');
      var on = g.querySelector('button.on');
      if(gid && on) data['tri_' + gid] = on.getAttribute('data-v');
    });
    return data;
  }
  function restore(data){
    if(!data) return;
    document.querySelectorAll('[data-save]').forEach(function(el){
      var id = el.getAttribute('data-save');
      if(!(id in data)) return;
      if(el.type === 'checkbox'){ el.checked = !!data[id]; }
      else { el.value = data[id]; }
    });
    document.querySelectorAll('.tri').forEach(function(g){
      var gid = g.getAttribute('data-tri');
      if(!gid) return;
      var v = data['tri_' + gid];
      if(!v) return;
      g.querySelectorAll('button').forEach(function(b){
        b.classList.toggle('on', b.getAttribute('data-v') === v);
      });
    });
  }
  var timer = null;
  function scheduleSave(){
    if(timer) clearTimeout(timer);
    timer = setTimeout(function(){
      try{ localStorage.setItem(KEY, JSON.stringify(collect())); }catch(e){}
      var tip = document.getElementById('saveTip');
      if(tip){
        tip.style.opacity = '1';
        setTimeout(function(){ tip.style.opacity = '0'; }, 1200);
      }
    }, 400);
  }

  function init(){
    try{
      var raw = localStorage.getItem(KEY);
      if(raw) restore(JSON.parse(raw));
    }catch(e){}
    scheduleSave();
  }

  /* ── 输入事件 ── */
  document.addEventListener('input', function(e){
    if(e.target.matches('[data-save]')) scheduleSave();
  });
  document.addEventListener('change', function(e){
    if(e.target.matches('[data-save]')) scheduleSave();
  });

  /* ── 三态按钮 ── */
  document.addEventListener('click', function(e){
    var b = e.target.closest('.tri button');
    if(!b) return;
    var g = b.closest('.tri');
    var cur = b.classList.contains('on');
    g.querySelectorAll('button').forEach(function(x){ x.classList.remove('on'); });
    if(!cur) b.classList.add('on');
    scheduleSave();
    if(typeof window.onTriChange === 'function') window.onTriChange();
  });

  /* ── 清空 ── */
  window.clearTool = function(){
    if(!confirm('确定清空本表单的全部填写内容吗？此操作不可撤销。')) return;
    document.querySelectorAll('[data-save]').forEach(function(el){
      if(el.type === 'checkbox') el.checked = false;
      else el.value = '';
    });
    document.querySelectorAll('.tri button').forEach(function(b){ b.classList.remove('on'); });
    try{ localStorage.removeItem(KEY); }catch(e){}
    if(typeof window.onTriChange === 'function') window.onTriChange();
  };

  /* ── 导出文本 ── */
  window.exportTool = function(title){
    var lines = [];
    lines.push('═══════════════════════════════');
    lines.push('  ' + (title || document.title));
    lines.push('═══════════════════════════════');
    // 先输出顶部 meta 字段
    document.querySelectorAll('.fill-meta .fm-row').forEach(function(row){
      var lb = row.querySelector('label');
      var ip = row.querySelector('input,select');
      if(lb && ip) lines.push(lb.textContent.replace(/[:：]\s*$/,'') + '：' + (ip.value || ''));
    });
    // 再输出各表格
    document.querySelectorAll('.sec').forEach(function(sec){
      var h = sec.querySelector('.sec-h');
      if(h) lines.push('\n【' + h.textContent.trim().replace(/^\d+\s*/,'') + '】');
      sec.querySelectorAll('table').forEach(function(tbl){
        var rows = tbl.querySelectorAll('tr');
        rows.forEach(function(tr, ri){
          var cells = [];
          tr.querySelectorAll('th,td').forEach(function(td){
            var ip = td.querySelector('input,textarea');
            var tri = td.querySelector('.tri button.on');
            var v;
            if(ip){
              v = ip.type === 'checkbox' ? (ip.checked ? '☑' : '☐') : ip.value;
            } else if(tri){
              v = tri.textContent.trim();
            } else {
              v = td.textContent.trim().replace(/\s+/g,' ');
            }
            cells.push(v);
          });
          lines.push(cells.join(' | '));
        });
      });
      // 区块内签名等
      sec.querySelectorAll('.sign').forEach(function(sg){
        var lb = sg.querySelector('.lb'), ip = sg.querySelector('input');
        if(lb) lines.push(lb.textContent.trim() + '：' + (ip && ip.value ? ip.value : ''));
      });
    });
    lines.push('\n═══════════════════════════════');
    lines.push('永州爱眼城眼镜连锁 · 闫胜君 整理');
    var txt = lines.join('\n');
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(txt).then(function(){
        alert('✅ 已复制到剪贴板：\n\n' + txt);
      }).catch(function(){ alert('内容如下（请手动复制）：\n\n' + txt); });
    } else {
      alert('内容如下（请手动复制）：\n\n' + txt);
    }
  };

  /* ── 打印 ── */
  window.printTool = function(){ window.print(); };

  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
