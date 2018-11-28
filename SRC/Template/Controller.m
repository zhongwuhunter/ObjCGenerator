//
//
//  Created by tiger
//
//

#import "${CLASSNAME}.h"
#import "${VIEWMODELNAME}.h"
#import "${BINDERNAME}.h"
#import "${VIEWNAME}.h"

@interface ${CLASSNAME} ()
@property (nonatomic, strong) ${BINDERNAME}      *binder;
@property (nonatomic, strong) ${VIEWMODELNAME}      *viewModel;
@end



@implementation ${CLASSNAME}

- (void)loadView{
    ${VIEWNAME} *aview = [[${VIEWNAME} alloc] initWithFrame:[UIScreen mainScreen].bounds];
    self.view = aview;
    self.binder = [[${BINDERNAME} alloc] initWithView:aview];
    self.viewModel = [${VIEWMODELNAME} new];
    [self.binder bindViewModel:self.viewModel];
}

- (void)viewDidLoad {
    [super viewDidLoad];
}

- (void)viewWillAppear:(BOOL)animated{
    [super viewWillAppear:animated];
    [self.binder viewWillAppear];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}









































@end
